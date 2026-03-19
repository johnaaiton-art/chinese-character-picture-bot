#!/usr/bin/env python3
"""
Anki export module for Vasilina Cards Bot.
/export command:
  - Reads this week's selected words from Google Sheet
  - Generates TTS audio for each word (Google Chirp3-HD, Chinese voices)
  - Creates Anki import .txt file
  - Zips everything and sends to Telegram
"""
import os, io, json, zipfile, tempfile, logging, requests
from datetime import datetime, timedelta
from google.oauth2.service_account import Credentials
from google.cloud import texttospeech
import gspread

log = logging.getLogger(__name__)

# Chinese Chirp3-HD voices — rotating
ZH_VOICES = [
    "cmn-CN-Chirp3-HD-Aoede",
    "cmn-CN-Chirp3-HD-Leda",
    "cmn-CN-Chirp3-HD-Puck",
    "cmn-CN-Chirp3-HD-Fenrir",
]

SCOPES_SHEETS = ["https://www.googleapis.com/auth/spreadsheets"]
SCOPES_TTS    = ["https://www.googleapis.com/auth/cloud-platform"]
SHEET_TAB     = "Vasilina Cards"

def get_creds(creds_path, scopes):
    return Credentials.from_service_account_file(creds_path, scopes=scopes)

def get_this_week_words(sheet_id, creds_path, days=7):
    """Read words added in the last `days` days from Google Sheet."""
    creds = get_creds(creds_path, SCOPES_SHEETS)
    gc = gspread.authorize(creds)
    sh = gc.open_by_key(sheet_id)
    try:
        ws = sh.worksheet(SHEET_TAB)
    except Exception:
        return []

    rows = ws.get_all_records()
    cutoff = datetime.now() - timedelta(days=days)
    words = []
    seen = set()
    for row in rows:
        try:
            ts = datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M")
        except Exception:
            continue
        if ts >= cutoff:
            word = row["Word (Chinese)"]
            if word and word not in seen:
                seen.add(word)
                words.append({
                    "chinese": word,
                    "pinyin":  row["Pinyin"],
                    "english": row["English"],
                    "card":    row.get("Card File", ""),
                })
    return words

def synthesise_chinese(text, voice_name, creds_path):
    """Call Google Cloud TTS and return MP3 bytes."""
    creds = get_creds(creds_path, SCOPES_TTS)
    client = texttospeech.TextToSpeechClient(credentials=creds)
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="cmn-CN",
        name=voice_name,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response.audio_content

def build_anki_export(words, creds_path):
    """
    Returns (zip_bytes, n_words, errors).
    Zip contains:
      - vasilina_anki.txt  (tab-separated: Chinese | Pinyin | English | [sound:filename.mp3])
      - *.mp3 files
    """
    anki_lines = []
    audio_files = {}   # filename -> bytes
    errors = []

    for i, w in enumerate(words):
        voice = ZH_VOICES[i % len(ZH_VOICES)]
        safe_name = w["chinese"].replace("/","_").replace(" ","_")
        audio_fname = f"vasilina_{safe_name}.mp3"

        try:
            mp3 = synthesise_chinese(w["chinese"], voice, creds_path)
            audio_files[audio_fname] = mp3
            sound_tag = f"[sound:{audio_fname}]"
        except Exception as e:
            log.error(f"TTS error for {w['chinese']}: {e}")
            errors.append(w["chinese"])
            sound_tag = ""

        # Anki import format: Chinese | Pinyin | English | Audio
        line = f'{w["chinese"]}\t{w["pinyin"]}\t{w["english"]}\t{sound_tag}'
        anki_lines.append(line)

    # build zip in memory
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        txt = "\n".join(anki_lines)
        zf.writestr("vasilina_anki.txt", txt)
        for fname, data in audio_files.items():
            zf.writestr(fname, data)
    buf.seek(0)
    return buf.read(), len(words), errors