from ast import FormattedValue
from ppadb.client import Client as AdbClient
import os


os.chdir(os.path.dirname(os.path.realpath(__file__)))



client = AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037
devices = client.devices()

if len(devices) == 0:
    print('No devices')
    quit()

device = devices[0]


#device.shell("screenrecord --time-limit 10 --verbose --size 480x848 /sdcard/demo.mp4")

def retrieve_files():
    file_extensions=[".mp3", ".m4a", ".3ga", ".aac", ".ogg", ".ga", ".wav", ".amr", ".aw", ".flac",
     ".mid", ".midi", ".xmf", ".mxmf", ".imy", ".rtttl", ".rtx", ".ota", ".ape", ".dsf", ".dff",
      ".ogg", ".mp4",".m4v",".3gp",".3g2",".avi",".flv",".mkv",".webm",".mov", ".ts", ".asf", ".mpg",
       ".mpeg", ".trp", ".wmv", ".vro", ".m2ts", ".mpo", ".bmp", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".heif"]
        
    unformatted_all_files = str((device.shell("ls -d /sdcard/*/").replace('\n', ""))).split(' ')

    
    
    sdcard_folders = str((device.shell("ls -d /sdcard/*/").replace('\n', ""))).split(' ')
    formatted_all_files = []
    


    
    for index in unformatted_all_files:
        if index == '':
            unformatted_all_files.remove(index)
        else:
            formatted_all_files.append(index)
    
    print(formatted_all_files)
    



    #device.pull("/sdcard/Android/data:com.amazon.mShop.android.shopping", 'dog')

retrieve_files()