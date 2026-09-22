#intro
#center: 10;66
#the ansi escape sequence is "\033[row;columH"
import sys
import time
from colorama import Fore, Style
from elements.rendering_engine import clear

lines = [
    r" __  __    _  _____ ____  ___  ____ _____ ____  ",
    r"|  \/  |  / \|_   _|  _ \|_ _|| ___|_____/ ___| ",
    r"| |\/| | / _ \ | | | |_) || | | |   |  _| \___   ",
    r"| |  | |/ ___ \| | |  _ < | | | |___| |___ ___) ",
    r"|_|  |_/_/   \_\_| |_| \_\___| \____|_____|____| "
]
start_row = 17
column = 45 #this part is for a bit later, i'm gonna need this once I build the next class for another part

text=(Fore.BLUE+"Running pure python 3.11 in the Command Line")

class TerminalIntro: #too many functions so i made a class to keep it organized

    def __init__(self, start_row=17, column=45):  #this is the initialization of the class, it sets up the starting row and column for the ASCII art and text
        self.start_row = start_row
        self.column = column
        self.text = f"{Fore.BLUE}Running pure python 6.11 in the Command Line"
        self.ASCII_LINES = lines 

    def clear(self):
        # This bridges the class calls directly to your global rendering engine import
        clear()

    def draw_ascii(self): 
        for i, line in enumerate(self.ASCII_LINES):
            sys.stdout.write(f"\033[{self.start_row + i};{self.column}H")
            sys.stdout.write(Fore.WHITE + line)
        sys.stdout.write(f"\033[{self.start_row + len(self.ASCII_LINES) + 1};1H")
        sys.stdout.flush()

    def simulate_code_run(self, filename, trigger_text): #scrolls through the text and looks REALLY cool
        try:
            with open(filename, 'r', encoding="utf-8") as f:
                for line in f:
                    if line.strip() != trigger_text:
                        print(Fore.GREEN + line, end="")
                        time.sleep(0.05)
                    else:
                        self.clear()
                        print(Style.RESET_ALL)
                        break
        except FileNotFoundError: #this is for when some idiot clones the repo and tries to modify the file without understanding the tree
            print(f"{Fore.RED}Error: {filename} not found.{Style.RESET_ALL}")
            time.sleep(1)

    def show_screen_one(self): #ok the rest should be pretty obvious
        self.draw_ascii()
        time.sleep(1.2)
        self.clear()

    def show_screen_two(self):
        self.draw_ascii()
        sys.stdout.write("\033[13;42H")
        print(self.text)
        time.sleep(1.4)
        self.clear()

    def show_screen_three(self):
        self.draw_ascii()
        sys.stdout.write("\033[13;39H")
        print(self.text, Style.RESET_ALL)
        sys.stdout.write("\033[14;39H")
        print("A project by Navigator0")
        time.sleep(1.2)
        self.clear()

    def play(self):
        self.show_screen_one()
        self.simulate_code_run("code.txt", "// Throws an exception if the HTTP status code is a failure")
        
        self.show_screen_two()
        self.simulate_code_run("code2.txt", "def getwidth():")
        
        self.show_screen_three()
