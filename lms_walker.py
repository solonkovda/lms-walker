#!/usr/bin/python3
import settings
import requests
import os
import filecmp
import shutil


def postprocess_text(text):
    #Hack to ignore the one existing additional course
    start_i = text.find('Creating Growth in a Post-windfall')
    finish_i = start_i + text[start_i:].find('</tr>')
    return text[:start_i] + text[finish_i:]


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
if r.status_code != 200:
    exit()

with open(settings.TMP_COURSE_FILE, 'w') as f:
    f.write(postprocess_text(r.text))
if not os.path.exists(settings.COURSE_FILE) or filecmp.cmp(
        settings.COURSE_FILE,settings.TMP_COURSE_FILE):
    shutil.move(settings.TMP_COURSE_FILE, settings.COURSE_FILE)
else:
    # Creating flag file
    with open(settings.FLAG_FILE_PATH, 'w') as f:
        pass
