# main animation page where everything is loaded together
#tbh this is a very lazy and messy way of doing it but WHO cares it works
import sys
import time
import os
from elements.cursor import showcursor, hidecursor
from elements.rendering_engine import clear

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

input()

clear()
import song

import elements.spinner
clear()
import elements.UI
time.sleep(0.3)
clear()
hidecursor()

from elements.intro import TerminalIntro

intro=TerminalIntro()
intro.play()