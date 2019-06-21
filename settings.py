import os
# Existence of the file is used for the notifier.
FLAG_FILE_PATH = 'flag.txt'

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')

# Id of chat to be notified
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Message to be sent
ALARM_MESSAGE = 'THE TIME HAS COME'
