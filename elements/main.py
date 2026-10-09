import json
from elements.rendering_engine import *
import random
import colorama
import string
import time
import threading
from pathlib import Path
import sys

json_path = Path(__file__).resolve().parent / "text.json"

with open(json_path, "r", encoding="utf-8") as file: #parse json file
    data = json.load(file)
txt1 = data["plaintext"]

lines = [txt1[str(i)] for i in range(len(txt1))] #get each line from the json file and store it in a list

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


