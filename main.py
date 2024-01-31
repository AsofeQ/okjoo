from os import system 
import os,sys,time,requests
import random, telebot, os
from time import sleep
from telebot import types
import requests
from os import system 
import os,sys,time,requests
try:
	Info = open("info.txt").read()
except:
	Info = "Ahmeed"	
if ":" not in Info:
	token = input("ToKeN : ");reqtoken = requests.get(f"https://api.telegram.org/bot{token}/getme").json();req = reqtoken["ok"]
	if req == True:
		id = input("ID : ")
		o = open("info.txt",'a').write(str(token)+'\n'+str(id))
		print("Done .")
	else:
		print("Erorr ToKeN .")
else:
	print("Ok .")
info = open("info.txt",'r').read();token = info.split('\n')[0];own_id = info.split('\n')[1]
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
		global id, name
		id = message.from_user.id
		name = message.from_user.first_name
		mar= types.ReplyKeyboardMarkup(resize_keyboard=True)
		try:
			y = open("ID.txt").read()
			user = y.replace("@", "")
		except:  
			user = "None"
		try:
			y = (open("sleep.txt").read())
			sleep = y.replace(" ", "")
		except:
			sleep = "0.0"
			B = types.KeyboardButton("Pin")
			D = types.KeyboardButton(f" Sleep {sleep} ")
			G = types.KeyboardButton("Run")
			H = types.KeyboardButton("Stop")
			R = types.KeyboardButton("Number")
			mar.add(G,H)
			mar.add(B)
			mar.add(D)
			mar.add(R)
			if str(id) == own_id:
				bot.send_message(message.chat.id,text="𝒘𝒆𝒍𝒄𝒐𝒎𝒆 , \n𝒊𝒏 𝒕𝒉𝒆 𝒄𝒉𝒆𝒄𝒌𝒆𝒓 𝒖𝒔𝒆𝒓 𝒏𝒂𝒎𝒆 𝒕𝒆𝒍𝒆𝒈𝒓𝒂𝒎 \n𝒅𝒆𝒗𝒆𝒍𝒐𝒑𝒆𝒅 𝒃𝒚 𝑶𝑴𝑨𝑹🇮🇶 @iii8i ."
				,reply_markup=mar)
				@bot.message_handler(func=lambda m:True)
				def text(message):
					acc = message.text
					id = message.from_user.id
					if str(id) == own_id:
						if acc == "Pin":
							bot.send_message(message.chat.id,text="Send Username")
						if "@" in acc:
								try:
										print(os.remove("ID.txt"))
								except:
										bot.send_message(message.chat.id, text="Dont Here User !")
								a = acc.replace("/ID", "")
								o = a.replace(" ", "")
								try:
									with open('ID.txt', 'a') as the_combo:
										the_combo.write(str(o))
									bot.send_message(message.chat.id, text="Done added User")
								except:
									bot.send_message(message.chat.id, text="This Error : Try Again")
						if "/sleep" in acc:
									try:
										os.remove("sleep.txt")
									except:
										pass
									a = acc.replace("/sleep", "")
									o = a.replace(" ", "")
									try:
										with open('sleep.txt', 'a') as the_combo:
											the_combo.write(str(o))
										bot.send_message(message.chat.id, text="Done Add Sleep")
									except:
										bot.send_message(message.chat.id, text="This Error : Try Again")
						if acc == "Run":
									try:
										bot.send_message(message.chat.id, text="Done.")
										system("php run.php")
									except:
										pass
						if acc == "Stop":
									try:
										system("php stop.php")
										bot.send_message(message.chat.id, text="Done.")
									except:
										pass
										bot.send_message(message.chat.id, text="Done .")
						if acc == "/RemoveAll":
										try:
											os.remove("Number.txt")
											bot.send_message(message.chat.id, text="- Done ")
										except:
												bot.send_message(message.chat.id, text="Dont There Number")
						if acc == "Number":
									bot.send_message(message.chat.id, text="1 - /RemoveAll To Deleted All Number \n 2 - /Count_Number To Know how many Number in bot \n 3 - /add with session ")
						if acc == "/Count_Number":
									try:
										document = open('Number.txt', 'rb')
										w = len(open("Number.txt").readlines())
										bot.send_document(message.chat.id,document,caption=f"- The Number  : {w}")
									except:
										bot.send_message(message.chat.id, text="Dont There Number")
						if "/add" in acc:
									ks = acc.replace("/add", "")
									k = ks.replace(" ", "")
									try:
										with open('Number.txt', 'a') as the_combo:
											the_combo.write(str(k)+'\n')
										bot.send_message(message.chat.id, text="Done Login")
									except:
										bot.send_message(message.chat.id, text="- Error , try Again.")
bot.polling(none_stop=True)