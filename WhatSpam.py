#-*- coding:utf-8 -*-
import requests
import json
import banner
import os,time
import colorama

from colorama import init,Fore,Back


init()




os.system("cls" or "clear")

def bann():
	banner.mostrar()
	
	
	

def spamm():	
	url = input("Agrega tu url con el token: ")
	num = input ("Agrega el numero de Whatsapp a Spamear [colocando el área del pais]: ")
	sms = str(input ("Agrega el sms [limite 1000 caracteres]: "))
	dat = input ("Cuantas veces se enviara: ")


	
	data = json.dumps({"phone": num , "body": sms})
	headers = {'Content-Type': 'application/json'}

	for i in range(0,int(dat)):

		res = requests.post(url, data=data, headers=headers)

		print (Fore.GREEN+"Archivo "+Fore.RESET+Fore.YELLOW+str(res.json())+Fore.RESET)

	print ("\n[!]- End\n")
	salir = input("Deseas salir o ir al menú [exit][menu] ")
	if salir == 'exit':
		os.system("cls" or "clear")

		exit()	
	if salir == 'menu':
		os.system ("cls" or "clear")
		main()


def SendFile():
	print("#Muy pronto!")
	
	#data = json.dumps({ "chatId": "","phone": "", "body": "NatureCover2001.jpg", "filename": "https://upload.wikimedia.org/wikipedia/ru/3/33/NatureCover2001.jpg","caption": "file text" })
	#headers = {'Content-Type': 'application/json'}
	#res = requests.post(url, data=data, headers=headers)
		#print (Fore.GREEN+"Archivo enviado "+Fore.RESET+str(res.json()))
	#print(res.json())

def SendPTT():
	print("#Muy pronto!")
	
	#data = json.dumps({"phone": "", "audio*":"https://firebasestorage.googleapis.com/v0/b/chat-api-com.appspot.com/o/audio_2019-02-02_00-50-42.ogg?alt=media&token=a563a0f7-116b-4606-9d7d-172426ede6d1"})
	
	#res = requests.post(url, data=data)
		#print (Fore.GREEN+"Archivo enviado "+Fore.RESET+str(res.json()))
	#print(res.json())


def main():
	bann()
	print("[1]- Spamm Whatsapp")
	print("[2]- File Whatsapp "+Fore.RED+"Pronto"+Fore.RESET)
	print ("[3]- Audio Whatsapp "+Fore.RED+"Pronto"+Fore.RESET)
	print ("[exit]- Salir \n")
	ent = input (Fore.GREEN+"D4rksit3-$ "+Fore.RESET)

	if ent == '1':
		spamm()
	if ent == '2':
		SendFile()
	if ent == '3':
		SendPTT()
	if ent == 'exit':
		
		os.system("cls" or "clear")

		exit()
	else:
		time.sleep(0.3)
		print ("[!]-Ingresaste un caracter incorrecto.")
		time.sleep(0.8)
		os.system("cls" or "clear")
		main()

main()



