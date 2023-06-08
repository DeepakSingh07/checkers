# This Script Extracts Udemy Links from these Telegram Channels https://t.me/coursefolder and https://t.me/Udemy4U.
# And shortens the links using cuty.io API.
# You have to share the links manually to the script
# ( Manual process for the time being as I didn't wanted to share each and every course from the channels. You can automate this if you want.)

import requests, os, time
import re
import telegram
import asyncio

async def send_message(token, chat_username, message):
    try:
        bot = telegram.Bot(token=token)
        message = await bot.send_message(chat_id=chat_username, text=message, parse_mode="Markdown", disable_web_page_preview=True)
        return message
    except telegram.error.TelegramError as e:
        print(f"Failed to send message: {e}")
        return None

global token ; token = "<ENTER YOUR BOT TOKEN HERE>"
global chat_username ; chat_username = '<ENTER YOUR CHANNEL USERNAME HERE>'

def coursefolder(x):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0'
    }

    response = requests.get(url=link, headers=headers)

    titlepattern = re.escape('<title>[100% Off] ') + '(.*?)' + re.escape(' - Course Folder</title>')
    titlematches = re.findall(titlepattern, response.text)
    title = titlematches[0]

    linkpattern = re.escape('udemy.com') + "(.*?)" + re.escape("','")
    linkmatches = re.findall(linkpattern, response.text)
    udemylink = 'https://udemy.com'+linkmatches[0]

    link_parts = udemylink.split('?couponCode=')

    LINK = link_parts[0]
    COUPON = link_parts[1]

    return title, LINK, COUPON

def courson(x):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 Edg/115.0.0.0'
    }

    response = requests.get(url=link, headers=headers)

    titlepattern = re.escape('<title>Coupon -\n') + '(.*?)' + re.escape('</title>')
    titlematches = re.findall(titlepattern, response.text)
    title = titlematches[0]

    linkpattern = re.escape('www.udemy.com/course/') + "(.*?)" + re.escape('">')
    linkmatches = re.findall(linkpattern, response.text)
    udemylink = 'https://udemy.com/course/'+linkmatches[0]

    link_parts = udemylink.split('?couponCode=')

    LINK = link_parts[0]
    COUPON = link_parts[1]

    return title, LINK, COUPON

while(True):
    print('''
    ██╗   ██╗██████╗ ███████╗███╗   ███╗██╗   ██╗
    ██║   ██║██╔══██╗██╔════╝████╗ ████║╚██╗ ██╔╝
    ██║   ██║██║  ██║█████╗  ██╔████╔██║ ╚████╔╝ 
    ██║   ██║██║  ██║██╔══╝  ██║╚██╔╝██║  ╚██╔╝  
    ╚██████╔╝██████╔╝███████╗██║ ╚═╝ ██║   ██║   LINK SHORTENER
     ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝   ╚═╝   
            [+] DEVELOPED BY DE3P4K [+]
    ''')
    link = input('Enter Link : ')

    if 'courson.xyz' in link:
        title, udemylink, coupon = courson(link)
    elif 'coursefolder.net' in link:
        title, udemylink, coupon = coursefolder(link)
    else:
        print('Invalid Link! Try Again.')
        time.sleep(1)
        os.system('cls')
        continue

    if title is None:
        print('Error Getting Title! Try Again.')
    elif udemylink is None:
        print('Error Getting Udemylink! Try Again.')

    print(title)

    link = f'https://cuty.io/api?api=<ENTER YOUR CUTY.IO API HERE>&url={udemylink}&format=text'

    shortlink = requests.get(url = link)
    print(shortlink.text)
    
    message = f'*{title}*\n_[ Free For First 1000 Enrolls Only! ]_\n\n{shortlink.text}\nUse Code : `{coupon}`'

    if title is None or shortlink is None:
        print('ERROR, Try Again.')
    else:
        loop = asyncio.get_event_loop()
        message_response = loop.run_until_complete(send_message(token, chat_username, message))
        # sent_message = send_message(token, chat_username, message)
        if message_response is not None:
            print("Message sent successfully!")
            time.sleep(1)
            os.system('cls')
        else:
            print("Failed to send message. Check the error output for details.")
            time.sleep(1)
            os.system('cls')
