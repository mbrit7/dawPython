"""
Author: Manuel Brito
Program a chronometer
"""

# I'm going to program a chronometer with minutes and seconds.
# A chronometer is a kind of watch that can measure time.
# When the chrono start the time increase and when finish, time is zero.
# If you wanna stop the chrono press 'ctrl + z'.

print("<<<CHRONO>>>\n")

from time import sleep
from colorama import Fore, init # for giving  some color to the chrono
init()

seconds = 0
minutes = 0

try:
    init_word = input("Write 'start' for start the program: ")
                
    if init_word == "start":
        while seconds < 60:
            # I stop the program every second for count the seconds   
            sleep(1) 
            seconds += 1
            print(Fore.CYAN+f"[{minutes}:{seconds}]")

            # when the seconds are equals zero I add a minute and 
            # restart the variable seconds
            if seconds == 60:
                minutes += 1
                seconds = 0
                print(f"[{minutes}:{seconds}]")
except:
    print("Err0r")











