from django.conf import settings
from django.core.mail import send_mail
import requests
import json


def send_msg(id, phone, text):
    payload = {
        "id": id,
        "phone": phone,
        "text": text
        }

    headers={'Content-Type':'application/json', 'Authorization': settings.TOKEN}
    r = requests.post(f'https://probe.fbrq.cloud/v1/send/{id}',data=json.dumps(payload), headers=headers)
    print(r.json()["code"])
    try:
        result = r.json()["code"]
        if result == 0:
            print('return true')
            return True
        else:return False 
    except:
        return False
    