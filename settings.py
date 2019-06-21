import os
# Existence of the file is used for the notifier.
FLAG_FILE_PATH = 'flag.txt'

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '')

# Id of chat to be notified
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', '')

# Message to be sent
ALARM_MESSAGE = 'THE TIME HAS COME'

LMS_LOGIN = os.environ.get('LMS_LOGIN', '')
LMS_PASSWORD = os.environ.get('LMS_PASSWORD', '')

# File to be compared in lms_walker
COURSE_FILE = 'courses.html'
TMP_COURSE_FILE = 'tmp.html'