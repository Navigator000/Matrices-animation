from elements.rendering_engine import *
import random
import colorama
import string

txt1 = "Matrices are mathematical tools that are used for various purposes, including but not limited to:"

with spinner(""):
    time.sleep(2)

clear()

def decrypt(txt, speed):
    pool = string.ascii_letters + string.digits + "!@#$"
    for i in range(len(txt) + 1):
        revealed = txt[:i]
        remaining_length = len(txt) - i
        scrambled = "".join(random.choice(pool) if not txt[i + j].isspace() else " " for j in range(remaining_length))
        sys.stdout.write("\r" + revealed + scrambled)
        sys.stdout.flush()
        time.sleep(speed)

clear()
decrypt(txt1, 0.05)


