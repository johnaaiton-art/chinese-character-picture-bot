#!/usr/bin/env python3
"""
Vasilina Chinese Character Cards Bot
- /next sends next card image with word buttons
- Tapping a word shows ✓ tick, keeps other buttons active
- ✅ Done logs selected words to Google Sheet + sends DeepSeek example sentences
- 😎 Already know all advances without logging
- /example after Done shows sentences for chosen words
"""
import os, json, time, logging, requests
from datetime import datetime
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import gspread
from google.oauth2.service_account import Credentials

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger(__name__)

# ── config ────────────────────────────────────────────────────────────────────
BOT_TOKEN    = os.environ["TELEGRAM_BOT_TOKEN"]
DEEPSEEK_KEY = os.environ["DEEPSEEK_API_KEY"]
SHEET_ID     = os.environ["GOOGLE_SHEET_ID"]
CREDS_PATH   = os.environ.get("GOOGLE_CREDS_PATH", "google-creds.json")
CARDS_DIR    = os.environ.get("CARDS_DIR", "output_png")
JSON_DIR     = os.environ.get("JSON_DIR", "json")
STATE_FILE   = "state.json"
SHEET_TAB    = "Vasilina Cards"

bot = telebot.TeleBot(BOT_TOKEN)

# ── state (persisted to disk) ─────────────────────────────────────────────────
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"card_index": 0, "selected": [], "current_card": None, "msg_id": None}

def save_state(s):
    with open(STATE_FILE, "w") as f:
        json.dump(s, f)

# ── card helpers ──────────────────────────────────────────────────────────────
def get_card_files():
    files = sorted(f for f in os.listdir(CARDS_DIR) if f.endswith(".png"))
    return files

def get_card_json(png_filename):
    slug = png_filename.replace(".png", ".json")
    path = os.path.join(JSON_DIR, slug)
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return None

def get_satellite_buttons(card_data, selected):
    """Build inline keyboard — one button per satellite word."""
    kb = InlineKeyboardMarkup(row_width=2)
    buttons = []
    for i, sat in enumerate(card_data["satellites"]):
        word = "".join(ch for ch, _ in sat["word"])
        label = f"{'✓ ' if i in selected else ''}{word} {sat['english']}"
        buttons.append(InlineKeyboardButton(label, callback_data=f"word_{i}"))
    kb.add(*buttons)
    # bottom row
    kb.row(
        InlineKeyboardButton("😎 Already know all", callback_data="skip"),
        InlineKeyboardButton("✅ Done", callback_data="done")
    )
    return kb

# ── Google Sheets ─────────────────────────────────────────────────────────────
def get_sheet():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file(CREDS_PATH, scopes=scopes)
    gc = gspread.authorize(creds)
    sh = gc.open_by_key(SHEET_ID)
    try:
        ws = sh.worksheet(SHEET_TAB)
    except gspread.WorksheetNotFound:
        ws = sh.add_worksheet(title=SHEET_TAB, rows=1000, cols=6)
        ws.append_row(["Timestamp", "Card", "Word (Chinese)", "Pinyin", "English", "Card File"])
    return ws

def log_to_sheet(card_data, card_file, selected_indices):
    try:
        ws = get_sheet()
        ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        card_name = card_data["char"]
        for i in selected_indices:
            sat = card_data["satellites"][i]
            word = "".join(ch for ch, _ in sat["word"])
            ws.append_row([ts, card_name, word, sat["pinyin"], sat["english"], card_file])
        log.info(f"Logged {len(selected_indices)} words to sheet")
    except Exception as e:
        log.error(f"Sheet error: {e}")

# ── DeepSeek ──────────────────────────────────────────────────────────────────
def get_example_sentence(word_chinese, word_english, pinyin):
    """Generate a short example sentence using words Vasilina already knows."""
    prompt = (
        f"Generate ONE short example sentence in Chinese using the word '{word_chinese}' ({pinyin}, {word_english}). "
        f"Rules: HSK 1-2 level vocabulary only (very simple words). "
        f"Max 10 characters. Include the Chinese sentence, pinyin, and English translation. "
        f"Format exactly like this:\n"
        f"Chinese: [sentence]\n"
        f"Pinyin: [pinyin]\n"
        f"English: [translation]"
    )
    try:
        r = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {DEEPSEEK_KEY}", "Content-Type": "application/json"},
            json={"model": "deepseek-chat", "max_tokens": 150,
                  "messages": [{"role": "user", "content": prompt}]},
            timeout=15
        )
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        log.error(f"DeepSeek error: {e}")
        return f"({word_chinese} — {word_english})"

# ── handlers ──────────────────────────────────────────────────────────────────
@bot.message_handler(commands=["start", "help"])
def cmd_start(msg):
    bot.send_message(msg.chat.id,
        "你好！👋\n\n"
        "Send /next to see your next character card.\n"
        "Tap words you want to add to Anki, then press ✅ Done.\n"
        "Press 😎 if you already know everything on the card.\n\n"
        "加油！💪"
    )

@bot.message_handler(commands=["next"])
def cmd_next(msg):
    state = load_state()
    cards = get_card_files()
    if not cards:
        bot.send_message(msg.chat.id, "No cards found!")
        return

    idx = state["card_index"] % len(cards)
    card_file = cards[idx]
    card_data = get_card_json(card_file)

    if not card_data:
        bot.send_message(msg.chat.id, f"Could not load card data for {card_file}")
        return

    # send image
    png_path = os.path.join(CARDS_DIR, card_file)
    with open(png_path, "rb") as f:
        kb = get_satellite_buttons(card_data, selected=set())
        sent = bot.send_photo(msg.chat.id, f, reply_markup=kb)

    state["card_index"] = idx + 1
    state["selected"] = []
    state["current_card"] = card_file
    state["msg_id"] = sent.message_id
    save_state(state)

@bot.message_handler(commands=["reset"])
def cmd_reset(msg):
    state = load_state()
    state["card_index"] = 0
    save_state(state)
    bot.send_message(msg.chat.id, "Card index reset to beginning. Send /next to start.")

@bot.callback_query_handler(func=lambda c: c.data.startswith("word_"))
def cb_word(call):
    state = load_state()
    card_data = get_card_json(state["current_card"])
    if not card_data:
        bot.answer_callback_query(call.id, "Card data not found")
        return

    idx = int(call.data.split("_")[1])
    selected = set(state["selected"])

    if idx in selected:
        selected.discard(idx)
        sat = card_data["satellites"][idx]
        word = "".join(ch for ch, _ in sat["word"])
        bot.answer_callback_query(call.id, f"Deselected: {word}")
    else:
        selected.add(idx)
        sat = card_data["satellites"][idx]
        word = "".join(ch for ch, _ in sat["word"])
        bot.answer_callback_query(call.id, f"✓ Selected: {word} — {sat['english']}")

    state["selected"] = list(selected)
    save_state(state)

    # update buttons in place to show ticks
    kb = get_satellite_buttons(card_data, selected)
    try:
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb)
    except Exception as e:
        log.warning(f"Edit markup error: {e}")

@bot.callback_query_handler(func=lambda c: c.data == "skip")
def cb_skip(call):
    bot.answer_callback_query(call.id, "😎 Great — moving on!")
    try:
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    except: pass
    bot.send_message(call.message.chat.id, "😎 Noted — you already know all of these!\nSend /next for the next card.")

@bot.callback_query_handler(func=lambda c: c.data == "done")
def cb_done(call):
    state = load_state()
    selected = list(set(state["selected"]))

    try:
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    except: pass

    if not selected:
        bot.answer_callback_query(call.id, "No words selected — tap words first, then Done")
        bot.send_message(call.message.chat.id,
            "You didn't select any words!\nTap the words you want to learn, then press ✅ Done.\n"
            "Or press 😎 if you already know them all.")
        return

    bot.answer_callback_query(call.id, "✅ Logged!")
    card_data = get_card_json(state["current_card"])

    # log to sheet
    log_to_sheet(card_data, state["current_card"], selected)

    # build summary
    lines = ["✅ Added to your Anki list:\n"]
    for i in sorted(selected):
        sat = card_data["satellites"][i]
        word = "".join(ch for ch, _ in sat["word"])
        lines.append(f"• {word} ({sat['pinyin']}) — {sat['english']}")
    lines.append("\n⏳ Getting example sentences from DeepSeek...")
    bot.send_message(call.message.chat.id, "\n".join(lines))

    # DeepSeek example sentences
    examples = []
    for i in sorted(selected):
        sat = card_data["satellites"][i]
        word = "".join(ch for ch, _ in sat["word"])
        sentence = get_example_sentence(word, sat["english"], sat["pinyin"])
        examples.append(f"📝 *{word}* ({sat['pinyin']}) — {sat['english']}\n{sentence}")

    if examples:
        bot.send_message(call.message.chat.id,
            "Here are some example sentences:\n\n" + "\n\n".join(examples),
            parse_mode="Markdown")

    bot.send_message(call.message.chat.id, "Send /next for the next card! 🎉")

    state["selected"] = []
    save_state(state)

# ── main ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    log.info("Vasilina Cards Bot starting...")
    bot.infinity_polling(timeout=30, long_polling_timeout=30)

# ── /export command ───────────────────────────────────────────────────────────
from export_anki import get_this_week_words, build_anki_export

@bot.message_handler(commands=["export"])
def cmd_export(msg):
    bot.send_message(msg.chat.id,
        "⏳ Fetching this week's words from Google Sheets and generating audio...\n"
        "This may take 30–60 seconds.")
    try:
        words = get_this_week_words(
            sheet_id=SHEET_ID,
            creds_path=CREDS_PATH,
            days=7
        )
        if not words:
            bot.send_message(msg.chat.id,
                "No words found from the last 7 days.\n"
                "Tap some word buttons on a card first, then press ✅ Done!")
            return

        bot.send_message(msg.chat.id,
            f"Found {len(words)} words. Generating TTS audio now... 🎵")

        zip_bytes, n, errors = build_anki_export(words, CREDS_PATH)

        # send zip
        import io
        bot.send_document(
            msg.chat.id,
            io.BytesIO(zip_bytes),
            visible_file_name=f"vasilina_anki_{datetime.now().strftime('%Y%m%d')}.zip",
            caption=(
                f"✅ Anki export ready!\n\n"
                f"📦 {n} words · 🎵 MP3 audio included\n\n"
                f"1. Unzip\n"
                f"2. Copy *.mp3 → your Anki media folder\n"
                f"3. Anki → File → Import → vasilina_anki.txt"
            )
        )
        if errors:
            bot.send_message(msg.chat.id,
                f"⚠️ TTS failed for: {', '.join(errors)}\n"
                f"These words are in the .txt but without audio.")

    except Exception as e:
        log.error(f"Export error: {e}")
        bot.send_message(msg.chat.id, f"❌ Export failed: {str(e)}")