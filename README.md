# Vasilina Chinese Character Cards Bot

## Folder structure on VM
```
~/vasilina-cards-bot/
├── bot.py                  # Telegram bot
├── generate_cards.py       # PNG generator (run once or to add new cards)
├── write_json.py           # Recreate all JSON files
├── requirements.txt
├── .env                    # secrets (never commit)
├── google-creds.json       # service account (never commit)
├── state.json              # auto-created, tracks card progress
├── json/                   # 27 card JSON files
│   ├── 01_dian.json
│   └── ...
└── output_png/             # 27 card PNG files
    ├── 01_dian.png
    └── ...
```

## .env file contents
```
TELEGRAM_BOT_TOKEN=xxx
DEEPSEEK_API_KEY=xxx
GOOGLE_SHEET_ID=xxx
VASILINA_TELEGRAM_ID=xxx
GOOGLE_CREDS_PATH=/home/yc-user/vasilina-cards-bot/google-creds.json
CARDS_DIR=/home/yc-user/vasilina-cards-bot/output_png
JSON_DIR=/home/yc-user/vasilina-cards-bot/json
```

## Setup on VM
```bash
ssh -i C:\Users\John\.ssh\id_rsa yc-user@178.154.198.14
cd ~
git clone https://github.com/johnaaiton-art/chinese-character-picture-bot.git vasilina-cards-bot
cd vasilina-cards-bot
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# create .env (see above)
# upload google-creds.json via scp
# generate PNGs
python3 generate_cards.py
# install and start service
```

## Systemd service
```bash
cat << 'SVCEOF' | sudo tee /etc/systemd/system/vasilina-cards-bot.service
[Unit]
Description=Vasilina Chinese Cards Bot
After=network.target
[Service]
Type=simple
User=yc-user
WorkingDirectory=/home/yc-user/vasilina-cards-bot
EnvironmentFile=/home/yc-user/vasilina-cards-bot/.env
ExecStart=/home/yc-user/vasilina-cards-bot/venv/bin/python bot.py
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
SVCEOF
sudo systemctl daemon-reload
sudo systemctl enable vasilina-cards-bot.service
sudo systemctl start vasilina-cards-bot.service
sudo systemctl status vasilina-cards-bot.service
```

## Adding new cards later
1. Edit write_json.py to add new card entries
2. Run: python3 write_json.py
3. Run: python3 generate_cards.py
4. git add . && git commit -m "Add new cards" && git push
5. On VM: git pull && sudo systemctl restart vasilina-cards-bot.service

## Commands
- /next — send next card
- /reset — go back to card 1
- /start or /help — show instructions
