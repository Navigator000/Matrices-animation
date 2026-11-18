import json
from elements.rendering_engine import *
lazy import random
from colorama import Fore, Back, Style
lazy import string
lazy import time
lazy import threading
from pathlib import Path
lazy import sys

json_path1 = Path(__file__).resolve().parent / "text.json"

with open(json_path1, "r", encoding="utf-8") as file: #parse json file
    data = json.load(file)
txt1 = data["plaintext"]

lines = {i: txt1[str(i)] for i in range(len(txt1))} #get each line from the json file and store it in a list
print(lines)
time.sleep(1000)
with spinner(""):
    time.sleep(2)

clear()

def decrypt(txt, speed):
    pool = string.ascii_letters + string.digits + "!@#$"
    for i in range(len(txt) + 1):
        revealed = txt[:i]
        remaining_length = len(txt) - i
        remaining_text = txt[i:]
        scrambled = "".join(random.choice(pool) if not remaining_text[j].isspace() else " " for j in range(remaining_length))
        sys.stdout.write("\r" + revealed + scrambled)
        sys.stdout.flush()
        time.sleep(speed)
    return

def isConnected(connectionID):
    if connectionID == "PBS07_BACKUP":
        return True
    else:
        return False

def checkConnection(connectionID):
    with spinner("Checking connection.."):
        time.sleep(2)   
    if isConnected(connectionID):
        print(f"{Fore.GREEN}Connection {connectionID} established.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Connection {connectionID} failed. Retrying...{Style.RESET_ALL}")
        count = 0
        while not isConnected(connectionID) and count < 2:
            with spinner("Reconnecting.."):
                time.sleep(2)
                count+=1
    return

def printErrorLogs(text):
    for line in text:
        print(f"{Fore.RED}Error: {line}{Style.RESET_ALL}")
    return

def weatherStation():
    

for line in lines:
    if line.strip():
        decrypt(line.strip(), 0.02)
        print()
        time.sleep(0.5)
    else:
        print()  # Print a blank line for empty lines
clear()

with spinner("Reconnecting.."):
    time.sleep(2)



