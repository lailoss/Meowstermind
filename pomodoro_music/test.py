# Pomodoro Timer with Music in Python
# By: Tom Ordonez
# The countdown function was inspired by an answer I saw on stackoverflow.
# Before running this program you need to: pip install python-vlc
# To run the program: python3 pomodoroTimer.py
# To modify the length of the Pomodoro just change the range of the countdown function
# Change the name of the mp3 files to your own files. They need to be placed
# in the same directory where tyou place this python file.
# If you have questions send me a message on LI: https://www.linkedin.com/in/tomordonez/

import vlc
import time
import sys

instance = vlc.Instance()
player = instance.media_player_new()

working = instance.media_new("Reverie.mp3")
coding = instance.media_new("Purple.mp3")

def countdown():
    for i in range(2700,0,-1):
        sys.stdout.write("\r")
        sys.stdout.write("Pomodoro: {:2d} seconds remaining.".format(i))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\nPomodoro Complete\n")

def focus():
    print("Are you working or coding?")
    focus = input()
    
    if focus == 'working':
        player.set_media(working)
        player.play()
        countdown()

    elif focus == 'coding':
        player.set_media(coding)
        player.play()
        countdown()
focus()