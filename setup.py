#!/bin/env python3
# code by : Termux Professor

"""

you can re run setup.py 
if you have added some wrong value

"""
import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
		
                                         
{re} █▀▄▀█ █▀█ █░░ █▀█ █▀▄▀█ █▄▄ █▀▀ █▄░█ █▄▀{cy}
 {re}█░▀░█ █▀▄ █▄▄ █▄█ █░▀░█ █▄█ ██▄ █░▀█ █░█{cy}
           Version : V.0
	{re} Attujuki Dalle #Paggurikie
	{cy}Ucapkan Bismillah Bosku 
	""")
banner()
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] enter api ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] enter hash ID : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] enter phone number : "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] Selesai Login Bosku!")
print(gr+"[+] Pindahki Lagi Penambah Group")
print(gr+"[+] Gunakan Komentar 'python scraper.py' ")
print(gr+"[+] Bismillah Mokki Bosku #PAGGURIKIE")
