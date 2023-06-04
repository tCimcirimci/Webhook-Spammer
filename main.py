from discord_webhook import DiscordEmbed, DiscordWebhook
import time
import requests
import colorama
import json
from colorama import Fore

colorama.init()

print("""
░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗░ ██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝ ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░ ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░░ ╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗ ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝ ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
Made by : Cimcirimci#2865
""")

def webhkspammer():
    webhook = input(Fore.BLUE + "Webhook URL: ")
    message = input(Fore.BLUE + "Message: ")

    while True:
        print(Fore.BLUE + "Sending --> " + message)
        print(Fore.RESET + " ")
        try:
            _data = requests.post(webhook, json={'content': message})

            if _data.status_code == 204:
                print(Fore.BLUE + "Sent --> " + message)
        except:
            print(Fore.RED + "Something Happend! / Probably Broken Webhook -> " + webhook)
            time.sleep(5)
            exit()

while True:
    webhkspammer()
