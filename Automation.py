import requests
import schedule
import time


def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': '5555555555',
        'message': 'message',
        'key': 'textbelt'
    })
    print(resp.json())


schedule.every().day.at('00:00').do(send_message)


while True:
    schedule.run_pending()
    time.sleep(1)
  
