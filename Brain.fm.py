import requests
import random
import string
import threading

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_account():
    url = 'https://v1.brain.fm/signup'

    headers = {
        'Origin': 'https://v1.brain.fm',
        'Referer': 'https://v1.brain.fm/redeem/gcp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0'
    }

    email = generate_random_string(10)

    payload = {
        "type": "SIGNUP",
        "email": f"{email}@yopmail.net",
        "password": "FightClub90!",
        "name": "DE3P4K",
        "token": "gcp",
        "consent": {},
    }

    response = requests.post(url=url, headers=headers, data=payload)
    if 'Signed up and logged in' in response.text:
        with open('brain.fmm.txt', 'a') as f:
            print(f'{email}@yopmail.net:FightClub90!')
            f.write(f'{email}@yopmail.net:FightClub90!\n')

def main():
    print('''
    
██████╗ ██████╗  █████╗ ██╗███╗   ██╗   ███████╗███╗   ███╗
██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║   ██╔════╝████╗ ████║
██████╔╝██████╔╝███████║██║██╔██╗ ██║   █████╗  ██╔████╔██║
██╔══██╗██╔══██╗██╔══██║██║██║╚██╗██║   ██╔══╝  ██║╚██╔╝██║
██████╔╝██║  ██║██║  ██║██║██║ ╚████║██╗██║     ██║ ╚═╝ ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝     ╚═╝
    ''')
    num = int(input('How Many Accounts to Generate? '))

    threads = []
    for _ in range(num):
        thread = threading.Thread(target=generate_account)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All accounts generated successfully.")

if __name__ == '__main__':
    main()
