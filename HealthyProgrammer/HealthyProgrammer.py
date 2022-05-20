# Healthy programmer
"""
9pm-5pm
Water - water.mp3 (3.5 litres) - Drank - log
Eyes - eyes.mp3  - eyDone - 30 min - log
Exercise - physical.mp3 - 45min - exDone - log

rules
pygame module to play audio

"""
from pygame import mixer
from datetime import datetime
from time import time


def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        word = input("Enter the word: ")
        if stopper == word:
            mixer.music.stop()
            break


def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{datetime.now()} : {msg}")


if __name__ == '__main__':

    init_water = time()
    init_eye = time()
    init_exercise = time()

    waterSec = 60 * 40
    eyeSec = 60 * 30
    exSec = 60 * 45

    while True:
        if time() - init_water > waterSec:
            print("Water Drinking time, Enter 'Drank' to stop the alarm.")
            musicloop("water.mp3", "drank")
            init_water = time()
            log_now("Drank Water!\n")

        if time() - init_eye > eyeSec:
            print("Give some rest to your eye. Enter 'eydone' to stop the alarm.")
            musicloop("eye.mp3", "eydone")
            init_eye = time()
            log_now("Given the rest to eye.\n")

        if time() - init_exercise > exSec:
            print("Do some exercise!. Enter 'exdone' to stop the alarm.")
            musicloop("exercise.mp3", "exdone")
            init_exercise = time()
            log_now("Done exercise!!\n")
