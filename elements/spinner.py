# beginning part
import time, threading
from colorama import Fore
from elements.cursor import hidecursor
from elements.rendering_engine import spinner

stop_spinner = threading.Event()

txt=['Initializing setup','Ping confirmed', 'Found station', 'Stabilising network', 'Verifying date', 'Searching for additional data','Setting up UI', 'Verifying modules', 'Encrypting connection', 'Finishing setup']

hidecursor()

with spinner(Fore.YELLOW+"Connecting to PBS07"): #pretty obvious
    time.sleep(0.5)
print(Fore.GREEN+"Connected!")

with spinner(Fore.YELLOW+"Loading data"):
    time.sleep(1.5)
print(Fore.GREEN+"All data loaded!")

for i in txt:
    with spinner(Fore.YELLOW + i):
        if i == "Initializing setup":
            time.sleep(0.5)
        elif i == "Encrypting connection":
            time.sleep(1)
        else:
            time.sleep(0.125)
print(Fore.GREEN+"Setup Complete!")
print(Fore.YELLOW+"Starting broadcast..")
time.sleep(0.3)