#intro
#center: 10;66
#the ansi escape sequence is "\033[row;columH"
import sys
import time
from colorama import Fore, Style

lines = [
    r" __  __    _  _____ ____  ___  ____ _____ ____  ",
    r"|  \/  |  / \|_   _|  _ \|_ _|| ___|_____/ ___| ",
    r"| |\/| | / _ \ | | | |_) || | | |   |  _| \___   ",
    r"| |  | |/ ___ \| | |  _ < | | | |___| |___ ___) ",
    r"|_|  |_/_/   \_\_| |_| \_\___| \____|_____|____| "
]
start_row = 17
column = 45
CLEAR_SCREEN=("\033[H\033[J")

for i, line in enumerate(lines):
    sys.stdout.write(f"\033[{start_row + i};{column}H")
    sys.stdout.write(Fore.WHITE+line)
    sys.stdout.flush()
print(f"\033[{start_row + len(lines) + 1};1H")

time.sleep(3)

sys.stdout.write(CLEAR_SCREEN)
