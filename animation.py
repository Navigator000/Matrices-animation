# main animation page where everything is loaded together
import sys
import time
import os
from elements.cursor import showcursor, hidecursor
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
CLEAR_SCREEN = "\033[H\033[J" # '\033[H' moves cursor to the top-left; '\033[J' clears everything below it

input()

sys.stdout.write(CLEAR_SCREEN)
import song

import elements.spinner
sys.stdout.write(CLEAR_SCREEN)
import elements.UI
time.sleep(0.1)
sys.stdout.write(CLEAR_SCREEN)
hidecursor()
import elements.intro