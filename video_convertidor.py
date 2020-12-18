from colorama import Fore, Style
import pafy
import sys
import os 

os.system("clear")
os.system("figlet CONVERTIDOR MP4")

 
#URL
download_url = input(Style.BRIGHT + Fore.RED + "URL: " + Style.NORMAL + Fore.WHITE)
video = pafy.new(download_url)
 
streams = video.streams
 
for i in streams:
        print(i)
 
#Mejor resolucion
best = video.getbest()
print(best.resolution, best.extension)
 
#Descarga - Directorio
best.download(filepath="video")
print(Fore.RED + "Video descargado correctamente!") 