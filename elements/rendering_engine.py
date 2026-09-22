import sys
import shutil

import sys
import shutil

def clear():
    clearscreen = "\033[H\033[J"  # '\033[H' moves cursor to the top-left; '\033[J' clears everything below it
    sys.stdout.write(clearscreen)
def getsize():
    columns, lines = shutil.get_terminal_size()
    return columns, lines

def render(x, y, text):
    sys.stdout.write("\033[%d;%dH" % (x, y))
    sys.stdout.write(text)
    sys.stdout.flush()

def center(text):
    columns, lines = getsize()
    x_center = lines // 2
    y_center = (columns // 2) - (len(text) // 2)
    render(x_center, y_center, text)

def left(text):
    columns, lines = getsize()
    x_left = lines // 2
    y_left = 1 + 2
    render(x_left, y_left, text)

def right(text):
    columns, lines = getsize()
    x_right = lines // 2
    y_right = columns - len(text) + 1
    render(x_right, y_right, text)


getsize()

clear()
render(10,4, "Hello!")
center("Hello!")
left("Hello!")
right("Hello!")