import pyrogram
import random
from pyrogram import client
from pyrogram import *
from pyrogram.types import *
import requests
from time import sleep
from pyrogram.raw import functions,types
from pyrogram.errors import FloodWait ,BadRequest
info = open("info.txt",'r').read();tok = info.split('\n')[0];idown = info.split('\n')[1]
r = open("ID.txt").read()
mk = r.replace("@", "")
o = mk.replace(" ", "")
qq = 0
ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text= - RuN -''')
req = requests.get(f"https://t.me/{o}").text
if "tgme_username_link" not in req:
	v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- The user is used')
	exit()
while True:
	for session in open("Number.txt","r").read().split("\n"):
		if session != "" and session != " ":
					app = Client("Mustafa",api_id=28354388,api_hash="5d5ed4a5fa795b367977221919fac806",session_string=session)
					app.connect()
					try:
						app.set_username(o)
						op = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=>Done<
- User : @{o}
- Clicks : {qq}
- Saved : Account
- Number : {app.get_me().phone_number}
===========================
* Mustafa ~ @Py_Iq''')
						qq+=1
					except FloodWait as e:
						qq+=1
					except BadRequest as e:
						qq+=1
					try:
						qq+=1
					except:
						qq+=1
					if qq == 10000:
						vv = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text={qq}')