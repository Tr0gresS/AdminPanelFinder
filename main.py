import os
import requests
from colorama import Fore , init

init()
print(Fore.CYAN+'''

    ___       __          _                              _________           __         
   /   | ____/ /___ ___  (_)___  ____  ____ _____  ___  / / ____(_)___  ____/ /__  _____
  / /| |/ __  / __ `__ \/ / __ \/ __ \/ __ `/ __ \/ _ \/ / /_  / / __ \/ __  / _ \/ ___/
 / ___ / /_/ / / / / / / / / / / /_/ / /_/ / / / /  __/ / __/ / / / / / /_/ /  __/ /    
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/ .___/\__,_/_/ /_/\___/_/_/   /_/_/ /_/\__,_/\___/_/     
                             /_/                                                    
                             
                             ''')


def adminpanel():
    while True:
        print(Fore.RED+"[+] Target https://. .com/ >> ",end="")
        target = input()
        if target[-1] == "/":
            with open("Wordlist","r",encoding="utf-8") as file:
                for i in file:
                    if i[0] != "/":
                        value = str(target + i[:-1])
                        try:
                            a = requests.get(value)
                            if a.status_code == 200 or a.status_code == 305:
                                print(Fore.BLUE + "[+] >> ", a.url)
                        except requests.exceptions.ConnectionError:
                            pass
        else:
            print(Fore.GREEN+"Tekrar Deneyin...")









if __name__ == "__main__":
    adminpanel()