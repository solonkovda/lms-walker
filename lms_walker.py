#!/usr/bin/python3
import settings
import requests
import os
import filecmp
import shutil

_LMS_LOGIN_URL = 'https://lms.hse.ru/index.php'
_LMS_COURSE_URL = 'https://lms.hse.ru/?sl'

if os.path.exists(settings.FLAG_FILE_PATH):
    # No need to recheck the course list if the change has been detected
    exit()

sess = requests.Session()
data = {
    '_qf__login_form': '',
    'user_login': settings.LMS_LOGIN,
    'user_password': settings.LMS_PASSWORD,
    'group1[userLogin]': 'Войти'
}

sess.post(_LMS_LOGIN_URL, data=data)

r = sess.get(_LMS_COURSE_URL)
with open(settings.TMP_COURSE_FILE, 'w') as f:
    f.write(r.text)
if not os.path.exists(settings.COURSE_FILE) or filecmp.cmp(
        settings.COURSE_FILE,settings.TMP_COURSE_FILE):
    shutil.move(settings.TMP_COURSE_FILE, settings.COURSE_FILE)
else:
    # Creating flag file
    with open(settings.FLAG_FILE_PATH, 'w') as f:
        pass
