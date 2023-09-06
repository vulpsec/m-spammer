#!/usr/bin/env python3
#*- coding: utf-8 -*--
#Coded by Morbius.os

AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'

Mor = '\033[95m'
Cyan = '\033[96m'
KoyuMavi = '\033[1;34m'
Mavi = '\033[94m'
Yeşil = '\033[92m'
Sarı = '\033[93m'
Kırmızı = '\033[91m'
Kalın = '\033[1m'
AltıÇizili = '\033[4m'
Bitir = '\033[0m'
Beyaz ='\033[1;37m'

import os
try:
    import pyautogui
except:
    os.system('pip install pyautogui')
import time

ali = input(f'Göndermek İstediğiniz Mesaj: {Yeşil}')
try:
    mehmet = int(input(f'{Beyaz}Mesajınız Kaç Saniye Aralıklarla Gönderilsin: {Yeşil}'))
except ValueError:
    while True:
        if ali == ali:
            print(Kırmızı+Kalın+'Lütfen Diğer Seferde Düzgün Bir Değer Gir!')
    
print('\n')
print(f"{Beyaz}Lütfen Mesajı Atmak İstediğiniz Platforma {Yeşil}(Whatsapp,İnstagram,Discord vb.) {Beyaz}Gidip Mesaj Yazma Kısmına Bir Kere Tıklayınız. {Kırmızı}{Kalın}10 Saniye Sonra Spam'a Başlanacaktır{Bitir}.Spam Sonunda Toplam Kaç Tane Mesaj Gönderdiğiniz Terminalinizde Yazacaktır.")
time.sleep(5)

süre = 10
print(f"{Kırmızı}{Kalın}Spam'ın Başlamasına {Yeşil}{süre}{Kırmızı} Saniye Kaldı.")
süre = süre-1
time.sleep(1)
print(f"{Kırmızı}{Kalın}Spam'ın Başlamasına {Yeşil}{süre}{Kırmızı} Saniye Kaldı.")
süre = süre-1
time.sleep(1)
print(f"{Kırmızı}{Kalın}Spam'ın Başlamasına {Yeşil}{süre}{Kırmızı} Saniye Kaldı.")
süre = süre-1
time.sleep(1)
print(f"{Kırmızı}{Kalın}Spam'ın Başlamasına {Yeşil}{süre}{Kırmızı} Saniye Kaldı.")
süre = süre-1
time.sleep(1)
print(f"{Kırmızı}{Kalın}Spam'ın Başlamasına {Yeşil}{süre}{Kırmızı} Saniye Kaldı.")
süre = süre-1
time.sleep(1)
print(f"{Kırmızı}{Kalın}Spam'ın Başlamasına {Yeşil}{süre}{Kırmızı} Saniye Kaldı.")
süre = süre-1
time.sleep(1)
print(f"{Kırmızı}{Kalın}Spam'ın Başlamasına {Yeşil}{süre}{Kırmızı} Saniye Kaldı.")
süre = süre-1
time.sleep(1)
print(f"{Kırmızı}{Kalın}Spam'ın Başlamasına {Yeşil}{süre}{Kırmızı} Saniye Kaldı.")
süre = süre-1
time.sleep(1)
print(f"{Kırmızı}{Kalın}Spam'ın Başlamasına {Yeşil}{süre}{Kırmızı} Saniye Kaldı.")
süre = süre-1
time.sleep(1)
print(f"{Kırmızı}{Kalın}Spam'ın Başlamasına {Yeşil}{süre}{Kırmızı} Saniye Kaldı.")
süre = süre-1
time.sleep(1)

print(Kırmızı+Kalın+'Spam Başlatılıyor...'+Beyaz)

def yolla(ğardaş):
    pyautogui.write(ğardaş)
    pyautogui.press('enter')
   
sayaç = 1
 
while True:
    yolla(ali)
    print(f"{Yeşil}{sayaç}{Beyaz} Tane Mesaj Gönderildi.")
    time.sleep(mehmet)
    sayaç = sayaç+1
    time.sleep(0)