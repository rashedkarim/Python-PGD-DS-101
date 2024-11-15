import keyboard

import time

i = 0
loader = "|/-\\"
index = 0
while True:
    time.sleep(.5)
    i+=1
    if keyboard.is_pressed(" "):
        break

    print(f"\r{loader[index]}", end="")
    index += 1
    index = 0 if index > 3 else index