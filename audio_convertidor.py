from colorama import Fore, Style
import pafy
import sys
import os

os.system("clear")
os.system("figlet CONVERTIDOR MP3") 

download_url = input(Style.BRIGHT + Fore.RED + "URL: " + Style.NORMAL + Fore.WHITE)
video = pafy.new(download_url) 
  
audiostreams = video.audiostreams 
for i in audiostreams: 
    print(i.bitrate, i.extension, i.get_filesize()) 
  
audiostreams[1].download()
print(Fore.RED + "Audio descargado correctamente!")  