# beginning part
import sys, time, threading
from contextlib import contextmanager
from itertools import cycle
from colorama import Fore
from elements.cursor import hidecursor

stop_spinner = threading.Event()

txt=['Initializing setup','Ping confirmed', 'Found station', 'Stabilising network', 'Verifying date', 'Searching for additional data','Setting up UI', 'Verifying modules', 'Encrypting connection', 'Finishing setup']
@contextmanager
def spinner(text, color=Fore.YELLOW):
    stop_event = threading.Event()
    chars = cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]) #<--- these are the frames of the animation.

    def animate():
        while not stop_event.is_set():
            sys.stdout.write(f"\r{next(chars)} {text}") #<--- tells the program to switch between frames
            sys.stdout.flush()
            time.sleep(0.09) #<--- time interval b/w frames. you can change if you want it to spin faster or slower.
            
    thread = threading.Thread(target=animate, daemon=True) #<--- initialization and beginning of animation
    thread.start()
    try:
        yield
    finally:
        stop_event.set()
        thread.join()
        sys.stdout.write("\r" + " " * (len(text) + 2) + "\r") #clears the text when its period is over
        sys.stdout.flush()

hidecursor()

with spinner(Fore.YELLOW+"Connecting to PBS07"):
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