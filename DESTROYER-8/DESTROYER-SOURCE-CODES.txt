import sys
import os
import time
import winsound as wskernels__
import random as rdkernels__
import subprocess as sbp
import colorama as ca
from colorama import Back,Fore,Style,Cursor

class mainF():
    def __init__(self):
        super().__init__()
        ca.init()
        print(Fore.RED)
        print(''' 
--------------------------------------------------------------------------------------------------
 ____  _____ ____ _____ ____   _____   _______ ____       _  _   
|  _ \| ____/ ___|_   _|  _ \ / _ \ \ / / ____|  _ \     | || |
| | | |  _| \___ \ | | | |_) | | | \ V /|  _| | |_) |____| || |_
| |_| | |___ ___) || | |  _ <| |_| || | | |___|  _ <_____|__   _|
|____/|_____|____/ |_| |_| \_\\___/ |_| |_____|_| \_\       |_|

(☻♣☻)Sen bilmiyor terminal kullanmak sen cahil o zaman kullanacak DESTROYER(☻♣☻)
              
--------------------------------------------------------------------------------------------------
              
''')
        print(Fore.LIGHTGREEN_EX)
        print('\n  ↓Eylem seç↓\b\b\b\n*1- Tarama İşlemleri\n*2-Değiştirme İşlemleri\n')
        xc=input('$> ')
        try:
            if xc=="1":
                try:
                    os.system('cls')
                    print('\n ↓Tarama türü seçin↓\n\b\b\b\n*1-Kök dizin taraması\n*2-Full tarama\n*3-Özel tarama\n*4-Çalışan Programları göster')
                    xf=input('#> ')
                    try:
                        if xf=='1':
                            print(Fore.LIGHTRED_EX,Style.DIM)
                            print(os.system('tree'))
                            print(Fore.LIGHTGREEN_EX,Style.NORMAL)
                            xg1=input('Çıkmak için (0) Başa dönmek için (1)\n£> ')
                            try:
                                if xg1=='0':
                                    try:
                                        sys.exit()
                                    except Exception as ext0kernel:
                                        print(f'hata: {ext0kernel}')
                            except Exception as kernels0:
                                print(f'hata: {kernels0}')
                            try:
                                if xg1=='1':
                                    try:
                                        os.system('cls')
                                        mainF()
                                    except Exception as ext1kernel:
                                        print(f'hata: {ext1kernel}')
                            except Exception as kernels1:
                                print(f'hata: {kernels1}')
                    except Exception as atg:
                        print(f'hata: {atg}')
                    try:
                        if xf=='2':
                            sw0=[
                            'Sys-4 waiting',
                            'sYs-4 waiting',
                            'syS-4 waiting',
                            'sys-4 Waiting',
                            'sys-4 wAiting',
                            'sys-4 waİting',
                            'sys-4 waiTing',
                            'sys-4 waitİng',
                            'sys-4 waitiNg',
                            'sys-4 waitinG'
                            ]
                            wskernels__.Beep(2500,100)
                            time.sleep(0.01)
                            wskernels__.Beep(2500,100)
                            time.sleep(0.01)
                            wskernels__.Beep(2500,100)
                            for g3f in range(20):
                                xfg=rdkernels__.randint(0,20)
                                if xfg<7:
                                    xfg=0
                                    pass
                                if xfg>11:
                                    break
                            wskernels__.Beep(2500,500)
                            for h in range(xfg):
                                time.sleep(0.1)
                                if h>8:
                                    h=1
                                print(f' {sw0[h]}','|',end="\r")
                                time.sleep(0.1)
                                print(f' {sw0[h]}','/',end="\r")
                                time.sleep(0.1)
                                print(f' {sw0[h]}','-',end="\r")
                                time.sleep(0.1)
                                print(f' {sw0[h]}','\\',end="\r")
                            print('\n\n\n↓↓MAİN SYSTEM FİLES FROM DESTROYER-4 LİST SYS↓↓\n\n\n')
                            print(Fore.LIGHTRED_EX,Style.BRIGHT)
                            wskernels__.Beep(2500,500)
                            print(os.system('dir /s'))
                            wskernels__.Beep(2500,500)
                            print(Fore.LIGHTGREEN_EX,Style.NORMAL)
                            sw1=[
                            'Sys waiting',
                            'sYs waiting',
                            'syS waiting',
                            'sys Waiting',
                            'sys wAiting',
                            'sys waİting',
                            'sys waiTing',
                            'sys waitİng',
                            'sys waitiNg',
                            'sys waitinG'
                            ]
                            for g3 in range(20):
                                xf=rdkernels__.randint(0,20)
                                if xf<7:
                                    xf=0
                                    pass
                                if xf>11:
                                    break
                            for g in range(xf):
                                time.sleep(0.1)
                                if g>8:
                                    g=1
                                print(f' {sw1[g]}','|',end="\r")
                                time.sleep(0.1)
                                print(f' {sw1[g]}','/',end="\r")
                                time.sleep(0.1)
                                print(f' {sw1[g]}','-',end="\r")
                                time.sleep(0.1)
                                print(f' {sw1[g]}','\\',end="\r")

                            print('\n\n\n↓↓ALL FİLES FROM DESTROYER-4 LİST SYS↓↓\n\n\n')
                            print(Fore.LIGHTRED_EX,Style.DIM)
                            wskernels__.Beep(2500,500)
                            print(os.system('dir /a'))
                            wskernels__.Beep(2500,500)
                            print(Fore.LIGHTGREEN_EX,Style.NORMAL)
                            xg1f=input('Çıkmak için (0) Başa dönmek için (1)\n£> ')
                            wskernels__.Beep(2500,500)
                            try:
                                if xg1f=='0':
                                    try:
                                        sys.exit()
                                    except Exception as ext0kernel:
                                        print(f'hata: {ext0kernel}')
                            except Exception as kernels0:
                                print(f'hata: {kernels0}')
                            try:
                                if xg1f=='1':
                                    try:
                                        os.system('cls')
                                        mainF()
                                    except Exception as ext1kernel:
                                        print(f'hata: {ext1kernel}')
                            except Exception as kernels1:
                                print(f'hata: {kernels1}')
                    except Exception as non_kernel_1xff:
                        print(f'hata: {non_kernel_1xff}')
                    try:
                        if xf=='3':
                            gfx=input('↓Hedef dosya yolunu gir↓\n\n##>> ')
                            print('\n\n SPECİAL FİLES \n\n')
                            print(Fore.LIGHTRED_EX,Style.DIM)
                            print(os.system(f'dir {gfx}'))
                            print(Fore.LIGHTGREEN_EX,Style.NORMAL)
                            xfim=input('\n\nÇıkmak için (0) Başa dönmek için (1)\n\n \b\b#>> ')
                            try:
                                if xfim=='0':
                                    sys.exit()
                            except Exception as kernel_dbases0:
                                print(f'hata: {kernel_dbases0}')
                            try:
                                if xfim=='1':
                                    os.system('cls')
                                    mainF()
                            except Exception as kernel_dbases1:
                                print(f'hata: {kernel_dbases1}')
                    except Exception as non_kernel_1xf:
                        print(f'hata: {non_kernel_1xf}')
                    try:
                        if xf=='4':
                            print('\n\n ↓CURRENT THREADİNG PROGRAMS↓ \n\n')
                            print(Fore.LIGHTRED_EX,Style.NORMAL)
                            wskernels__.Beep(2500,500)
                            print(os.system(f'tasklist'))
                            wskernels__.Beep(2500,500)
                            print(Fore.LIGHTGREEN_EX,Style.DIM)
                            xfim=input('\n\nÇıkmak için (0) Başa dönmek için (1)\n\n \b\b#>> ')
                            try:
                                if xfim=='0':
                                    sys.exit()
                            except Exception as kernel_dbases2:
                                print(f'hata: {kernel_dbases2}')
                            try:
                                if xfim=='1':
                                    os.system('cls')
                                    mainF()
                            except Exception as kernel_dbases3:
                                print(f'hata: {kernel_dbases3}')
                    except Exception as non_kernel_1xf:
                        print(f'hata: {non_kernel_1xf}')
                except Exception as kernel_dat2:
                    print(f'hata: {kernel_dat2}')
        except Exception as kernel_dat1:
            print(f'hata: {kernel_dat1}')
        try:
            if xc=='2':
                print('\n\n*1-Başlatma\n*2-Silme\n*3-Path(yol) bulma')
                xcfg0=input('$>> ')
                try:
                    if xcfg0=='1':
                        sinput0=input('\n\n↓Başlatılacak programın yolunu gir↓\n\n#>> ')
                        try:
                            print('\nProgram Çalıştırılıyor...')
                            time.sleep(2)
                            os.system('cls')
                            print(f'\n\nProgram durumu: ACİK\nProgram yolu: {sinput0}\nUzantı: .exe\nHeader(baslik): YOK')
                            os.system(f'start {sinput0}')
                            cinput0=input('\n\nÇıkmak için (0) Başa dönmek için (1)\n\n#> ')
                            if cinput0=='0':
                                try:
                                    sys.exit()
                                except Exception as kernel_ext_hdr_err0:
                                    print(f'hata: {kernel_ext_hdr_err0}')
                            if cinput0=='1':
                                try:
                                    os.system('cls')
                                    mainF()
                                except Exception as statements_errhdr0_non_kernel:
                                    print(f'hata: {statements_errhdr0_non_kernel}')
                        except Exception as kernel_header_err0:
                            print(f'hata: {kernel_header_err0}')
                except Exception as kernel_sdb0:
                    print(f'hata: {kernel_sdb0}')
                try:
                    if xcfg0=='2':
                        sinput0=input('\n\nSilinecek programın yolunu gir↓\n\n#>> ')
                        try:
                            print('\nProgram Siliniyor...')
                            time.sleep(2)
                            os.system('cls')
                            print(f'\n\nProgram durumu: SİLİNDİ\nProgram yolu: {sinput0}\nUzantı: (?)\nHeader(baslik): (?)')
                            os.system(f'del {sinput0}')
                            cinput0=input('\n\nÇıkmak için (0) Başa dönmek için (1)\n\n#> ')
                            if cinput0=='0':
                                try:
                                    sys.exit()
                                except Exception as kernel_ext_hdr_err1:
                                    print(f'hata: {kernel_ext_hdr_err1}')
                            if cinput0=='1':
                                try:
                                    os.system('cls')
                                    mainF()
                                except Exception as statements_errhdr0_non_kernel1:
                                    print(f'hata: {statements_errhdr0_non_kernel1}')
                        except Exception as kernel_header_err1:
                            print(f'hata: {kernel_header_err1}')
                except Exception as kernel_sdb1:
                    print(f'hata: {kernel_sdb1}')
                try:
                    if xcfg0=='3':
                        sinput0=input('\n\nBulunacak programın yolunu gir↓\n#>> ')
                        try:
                            print('\nProgram Bulunuyor...')
                            time.sleep(2)
                            os.system('cls')
                            g=sbp.run(['where',sinput0],capture_output=True,text=True)
                            gr0=g.stdout
                            print(Fore.LIGHTRED_EX,Style.DIM)
                            print(gr0)
                            print(Fore.LIGHTGREEN_EX,Style.NORMAL)
                            cinput0=input('\nÇıkmak için (0) Başa dönmek için (1)\n\n#> ')
                            if cinput0=='0':
                                try:
                                    sys.exit()
                                except Exception as kernel_ext_hdr_err2:
                                    print(f'hata: {kernel_ext_hdr_err2}')
                            if cinput0=='1':
                                try:
                                    os.system('cls')
                                    mainF()
                                except Exception as statements_errhdr0_non_kernel2:
                                    print(f'hata: {statements_errhdr0_non_kernel2}')
                        except Exception as kernel_header_err2:
                            print(f'hata: {kernel_header_err2}')
                except Exception as kernel_sdb2:
                    print(f'hata: {kernel_sdb2}')
        except Exception as kernel_err0:
            print(f'hata: {kernel_err0}')
        except Exception as kernel_err0:
            print(f'hata: {kernel_err0}')

mainF()