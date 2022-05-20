# importing modules 
from pygame import mixer
import os

# Changing directory 
os.chdir("songs")
# getting the list of all song in songs directory
songs_list = os.listdir()

print("============================================")
print("WELCOME TO MY MUSIC SYSTEM")
while True:
    option = input("""What do you wanna do:
😋. Show      😍. Play
👉👉 """).lower()
    print("============================================")

    # to show all the song list to user 
    if option == "show":
        print("=========🎵 SONGS LIST 🎵 =========")
        for song in songs_list:
            if song.endswith("mp3"):
                print(f"{songs_list.index(song) + 1} . {song.upper()} 😋")
        print("=============================")

    # to play the song 
    elif option == "play":
        music = int(input("Which song you want to play: "))
        print(f"Listening - {songs_list[music - 1]} 😍\n")
        mixer.init()
        mixer.music.load(f"{songs_list[music - 1]}")
        mixer.music.play()
        while True:
            choose = input("""🤔. Pause      😅. Resume       😖. Restart      😏. Stop
👉👉 """)
            # to pause the song 
            if choose == "pause":
                print("You have paused song. 🤨\n")
                mixer.music.pause()

            # to resume the song 
            elif choose == "resume":
                print(f"Listening - {songs_list[music - 1]} 😍\n")
                mixer.music.unpause()

            # to restart the song 
            elif choose == "restart":
                print(f"Listening - {songs_list[music - 1]} 😍\n")
                mixer.init()
                mixer.music.load(f"{songs_list[music - 1]}")
                mixer.music.play()

            # to stop the song 
            elif choose == "stop":
                print("You stopped the song. 😥\n")
                mixer.music.stop()
                break

            # if you will given invalid input 
            else:
                print("Invalid input. 😑\n")

    # if you will given invalid input 
    else:
        print("Invalid input. 😑")
