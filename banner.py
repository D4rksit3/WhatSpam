import colorama
import base64
from colorama import init,Fore,Back
init()

def mostrar():
	bann = Fore.GREEN+"""
	·▄▄▄▄   ▄▄▄· ▄▄▄  ▄ •▄ .▄▄ · ▪  ▄▄▄▄▄▄▄▄ .
	██▪ ██ ▐█ ▀█ ▀▄ █·█▌▄▌▪▐█ ▀. ██ •██  ▀▄.▀·
	▐█· ▐█▌▄█▀▀█ ▐▀▀▄ ▐▀▀▄·▄▀▀▀█▄▐█· ▐█.▪▐▀▀▪▄
	██. ██ ▐█ ▪▐▌▐█•█▌▐█.█▌▐█▄▪▐█▐█▌ ▐█▌·▐█▄▄▌
	▀▀▀▀▀•  ▀  ▀ .▀  ▀·▀  ▀ ▀▀▀▀ ▀▀▀ ▀▀▀  ▀▀▀ 

	"""+Fore.RESET
	print(format(bann,">50s") )