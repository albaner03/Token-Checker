import os
from colorama import Fore
import time
import sys
import requests
import tkinter
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import requests
import sys

Tk().withdraw()
root = tkinter.Tk()
root.withdraw()


def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.05)


def RPT():
    while 1:
        Diablo()
        os.system("pause")


def Diablo():
    global raw
    os.system("cls && title 𝕯𝖎𝖆𝖇𝖑𝖔 𝓿𝟏.𝟎")
    design = """
\u001b[38;5;46m                                                 ▄▄▄▄▀ \u001b[38;5;47m████▄ \u001b[38;5;48m█  █▀ \u001b[38;5;49m▄███▄   \u001b[38;5;50m   ▄   
\u001b[38;5;46m                                              ▀▀▀ █    \u001b[38;5;47m█   █ \u001b[38;5;48m█▄█   \u001b[38;5;49m█▀   ▀  \u001b[38;5;50m    █  
\u001b[38;5;46m                                                  █    \u001b[38;5;47m█   █ \u001b[38;5;48m█▀▄   \u001b[38;5;49m██▄▄    \u001b[38;5;50m██   █ 
\u001b[38;5;46m                                                 █     \u001b[38;5;47m▀████ \u001b[38;5;48m█  █  \u001b[38;5;49m█▄   ▄▀ \u001b[38;5;50m█ █  █ 
\u001b[38;5;46m                                                ▀      \u001b[38;5;47m      \u001b[38;5;48m  █   \u001b[38;5;49m▀███▀   \u001b[38;5;50m█  █ █ 
\u001b[38;5;46m                                                       \u001b[38;5;47m      \u001b[38;5;48m ▀    \u001b[38;5;49m        \u001b[38;5;50m█   ██ 

\u001b[38;5;46m                                                    Made by albaner#0001
                                    

    """
    print(design)
    time.sleep(3)
    while True:
        combo_filename = askopenfilename(filetypes=(("Text File", "*.txt"), ("All Files", "*.*")), title="Choose Your unchecked TokensList!")
        try:
            with open(combo_filename, 'r') as UseFile:
                print(f'{Fore.LIGHTWHITE_EX}[{Fore.BLUE}Combo{Fore.RED}List:{Fore.LIGHTWHITE_EX}] ' + Fore.LIGHTGREEN_EX + combo_filename)
                tokensline = sum(1 for _ in UseFile)
            break
        except:
            print(f'{Fore.RED} [{Fore.LIGHTGREEN_EX}-{Fore.RED}] Not existing combo File')
            time.sleep(1)
            continue

    print(f'{Fore.LIGHTWHITE_EX}[{Fore.BLUE}Combo{Fore.RED}List:{Fore.LIGHTWHITE_EX}] ' + Fore.LIGHTGREEN_EX + str(tokensline))
    print("")
    print(Fore.BLUE + "Starting " + Fore.RED + "Checking")
    time.sleep(2)
    print("")
    with open(combo_filename, 'r') as f:
        tokens = f.readlines()
        for x in tokens:
            token = x.rstrip()
            api = requests.get('https://discordapp.com/api/v6/users/@me/library', headers={'authorization': token})
            if api.status_code == 200:
                print(Fore.LIGHTGREEN_EX)
                print(f'[+] {token}')
                with open('WorkingTokens.txt', 'a') as c:
                    c.write(f'{token}\n')
            
            else:
                print(Fore.RED)
                print(f'[-] {token}')
    print("")
    print("Done Checking!")
    print("")


RPT()
