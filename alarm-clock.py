#-------------------------------------------------------------------------------
# Name:        Alarm Clock/Timer
# Purpose:
#
# Author:      ramojo
#
# Created:     18/02/2023
# Copyright:   (c) ramojo 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Alarm sound from https://cdn.pixabay.com/download/audio/2022/03/15/audio_6829ae637d.mp3?filename=031974_30-seconds-alarm-72117.mp3

from playsound import playsound
import time

# Add ANSI Charactrs
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 # // is used for integer divide. It only gives the integer not the remainder
        seconds_left = time_left % 60 # Modular gives us the remainder only
        print(f"{CLEAR_AND_RETURN} The alarm will sound in: {minutes_left:02d}:{seconds_left:02d}") # 02d means make the variable 2 digits if it isnt and pad it with a zero (add a zero at the begining of a single digit)

    playsound("alarm-sound.mp3")

if __name__ == '__main__':
    minutes = int(input("How many minutes should the alarm wait: "))
    seconds = int(input("How many seconds should the alarm wait: "))

    total_seconds = (minutes * 60) + seconds

    alarm(total_seconds)
