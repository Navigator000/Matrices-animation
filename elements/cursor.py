#cursor
import sys

def hidecursor():
    sys.stdout.write("\033[?25l") #<---"\033[?25l" is an escape sequence used to hide the cursor. only works in Unix OS!
    sys.stdout.flush()


def showcursor():
    sys.stdout.write("\033[?25h") #<---"\033[?25h" is an escape sequence used to show the cursor. onky works in Unix OS!
    sys.stdout.flush()