import sys
import shutil
import time
from colorama import *
from contextlib import contextmanager
import threading
from itertools import cycle

#welcome to the rendering engine
#this was surprisingly easy to make, and it works on both Windows and Linux (kind of)!

just_fix_windows_console()

def clear():
    clearscreen = "\033[H\033[J"  # '\033[H' moves cursor to the top-left; '\033[J' clears everything below it
    sys.stdout.write(clearscreen)

def getsize(): #here we get the size using shutil.get_terminal_size() which returns a tuple of (columns, lines)
    columns, lines = shutil.get_terminal_size()
    return columns, lines

def render(x, y, text): #this is for when the text needs to be custom rendered at specific coordinates (x, y) in the terminal. x is the row number, y is the column number
    sys.stdout.write("\033[%d;%dH" % (x, y))
    sys.stdout.write(text)
    sys.stdout.flush()

def center(text): #auto center
    columns, lines = getsize()
    x_center = lines // 2
    y_center = (columns // 2) - (len(text) // 2)
    render(x_center, y_center, text)

def left(text): #autoleft
    columns, lines = getsize()
    x_left = lines // 2
    y_left = 1 + 2
    render(x_left, y_left, text)

def right(text): #same same except youknow, right
    columns, lines = getsize()
    x_right = lines // 2
    y_right = columns - len(text) + 1
    render(x_right, y_right, text)

def top_left(text):
    render(1, 1, text)

def top_right(text):
    columns, lines = getsize()
    y_right = columns - len(text) + 1
    render(1, y_right, text)

def bottom_left(text):
    columns, lines = getsize()
    render(lines, 1, text)

def bottom_right(text):
    columns, lines = getsize()
    y_right = columns - len(text) + 1
    render(lines, y_right, text)

def center_top(text):
    columns, lines = getsize()
    y_center = (columns // 2) - (len(text) // 2)
    render(1, y_center, text)

def center_bottom(text):
    columns, lines = getsize()
    y_center = (columns // 2) - (len(text) // 2)
    render(lines, y_center, text) 

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

getsize()

clear()
render(10,4, "Hello!")
center("Hello!")
left("Hello!")
right("Hello!")