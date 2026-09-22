#remember: \033[Row;ColumnH if you want to position a UI
#Your Grid Size: 133 columns wide x 37 rows tall (37;133) (1920x1200 is my laptop size)
#center: 10;66
#yes i know there is an easier way using libraries like curses and textual and whatnot but
#im gonna do it the hard way and build this by hand
#tony stark built his suit with a hammer
#using scrap metal
#in a cave (or den? whatever)

import time
import sys
from colorama import Fore,Style
from elements.cursor import showcursor
import threading

mountain_stop_event = threading.Event()

mountain_canvas = [
    r"      /\                                      /\                               /\           ", #<--- beautiful mountains that will autoscroll above the text
    r"     /  \  /\                  /\            /  \      /\                     /  \/\        ",
    r"    /    \/  \       /\       /  \          /    \    /  \                   /      \       ",
    r"___/          \_____/  \_____/    \________/      \__/    \___________/\____/        \______"
]


def draw_scrolling_background(offset): #ok im gonna be fr here
    sys.stdout.write(Fore.WHITE + Style.DIM)
    for i, line in enumerate(mountain_canvas):
        start_pos = offset % len(line)
        frame_slice = (line[start_pos:] + line[:start_pos])[:90]
        sys.stdout.write(f"\033[{4 + i};1H{frame_slice}")
    sys.stdout.write(Style.RESET_ALL)

def background_mountain_loop():
    bg_offset = 0
    while not mountain_stop_event.is_set():
        draw_scrolling_background(bg_offset)
        bg_offset += 1
        time.sleep(0.1)
        
sys.stdout.write("\033[1;58H") 
print("WEATHER STATION REPORT")
sys.stdout.write("\033[2;54H") 
print("Location: Boston, Massachussets")

weatherinfo=[ #weather info for later 
    ("Date:", "22/10/2009"),
    ("Chance of Rain:", "20%"),
    ("Precipitation:", "NaN"),
    ("AVG wind speed:", "7.4mph")
]

sys.stdout.write("\033[12;98H") 
print(Fore.YELLOW+"====================================")

for index, (label, value) in enumerate(weatherinfo, start=13): #prints weather info cleanly
    sys.stdout.write(f"\033[{index};100H")
    print(f"{Fore.BLUE}{label} {Style.RESET_ALL}{value}")

for i in range(13,17):
    sys.stdout.write(f"\033[{i};98H" + Fore.YELLOW + "|")
    sys.stdout.write(f"\033[{i};134H" + Fore.YELLOW + "|")

sys.stdout.write("\033[17;98H") 
print(Fore.YELLOW+"====================================", Style.RESET_ALL) #closes it up

def typewriter(text, delay=0.075, color=Fore.BLUE): #the subtitles will be out of sync for most of the beginning. this is partly intentional and partly a result of "i dont understand the solution"
    showcursor() #<--- mostly for that cool effect
    words = text.split()
    trigger_words = ["i-495", "boston", "22nd", "midnight", "mph", "25mph", "sunny"] #this is where the text is made to pause
    pause_duration = 0.6
    stop_word="High-igh-igh-igh-igh-igh"
    track=""
    

    current_row = 10 #text position start
    current_col = 1

    for word in words:
        if current_col + len(word) > 90:
            current_row += 1
            current_col = 1

        for char in word:
            sys.stdout.write(f"\033[{current_row};{current_col}H")
            
            print(color+char, end="", flush=True)
            time.sleep(delay)
            current_col += 1
            
            track+=char
            if track.endswith(stop_word):
                print()
                weatherinfo=[ #weather info for later 
                ("Date:", "22/10/2009"),
                ("Chance of Rain:", "??%"),
                ("Precipitation:", "???"),
                ("AVG wind speed:", "??mph")
            ]
                for index, (label, value) in enumerate(weatherinfo, start=13): #prints weather info 
                    sys.stdout.write(f"\033[{index};100H")
                    print(f"{Fore.BLUE}{label} {Style.RESET_ALL}{value}")
                return
            
        sys.stdout.write(f"\033[{current_row};{current_col}H")
        print(" ", end="", flush=True)
        current_col += 1
        
        clean_word = word.lower().strip(".,;:!?")

        if clean_word in trigger_words: 
            current_row += 1
            current_col = 1
            if clean_word!="22nd" and clean_word!="25mph" and clean_word!="sunny":
                time.sleep(pause_duration)
            elif clean_word=="22nd":
                time.sleep(pause_duration+0.3)  
            elif clean_word=="25mph":
                time.sleep(pause_duration+1.2)
            else:
                pass

sys.stdout.write("\033[10;1H") #this reads the file contents present in media. in the file you will find the entire file
text="media/credits.txt"
with open(text, 'r') as f:
    raw=f.read()
    filecont=" ".join(raw.split())
    
    mountain_stop_event.clear()
    mountain_thread = threading.Thread(target=background_mountain_loop, daemon=True)
    mountain_thread.start()
    
    typewriter(filecont)
    
    mountain_stop_event.set()
    mountain_thread.join()
