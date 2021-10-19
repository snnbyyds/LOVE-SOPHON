#PREP
import time   #time
from pygame import mixer   
from colorama import Fore,Back,Style,init  #colour
init(autoreset = True)    #color auto reset

#AUDIO
mixer.init()
#unlock=() not used
shutdown=mixer.Sound("Windows Shutdown.wav")
exc=mixer.Sound("Windows Exclamation.wav")
ding=mixer.Sound("Windows Ding.wav")
stop=mixer.Sound("Windows Critical Stop.wav")
stop.set_volume(0.6)
ding.set_volume(0.6)
exc.set_volume(0.6)
shutdown.set_volume(0.6)
background=("TheFatRat-Unity.mp3")
mixer.music.load(background)
mixer.music.set_volume(0.1)
mixer.music.play()

#ABOUT "love Sophon" programme
print(Fore.YELLOW + "============================ABOUT=====================================")
ver=str("v0.2.2");author=str("sn")
intro=str("SOPHON=GOD! I'll FUCK anyone who doesn't like Sophon")
print(Fore.RED + "LOVE SOPHON",ver,Fore.GREEN + ".stable")
time.sleep(0.2777)
print(Fore.GREEN + "author:",author)
time.sleep(0.2777)
exc.play()
print(Fore.RED + intro)
print()

#CHANGELOG
print(Fore.GREEN + "============================CHANGELOG=================================")
print("1.BACKGROUND MUSIC")
print("2.REMOVED A SOUND EFFECT TO AVOID CRASH") #bug
print("3.COLOUR ADDED")
print()

#PAUSE
time.sleep(2.2216)

#START
line=str(Fore.GREEN + "===========================START!===================================")
ding.play()
print(line)
time.sleep(1.1108)
print()
print(Fore.GREEN + "Do you",Fore.RED + "love Sophon? ")
time.sleep(1.1108)
love=str(input("Input:"))

if love == "yes" or love == "YES" or love == "1" or love == "y":
           print(Fore.GREEN + "GREAT")
           ding.play()
           time.sleep(0.5554)
           print(Fore.GREEN + "GOD SOPHON!!")
           ding.play()

elif love == "no" or love == "NO" or love == "2" or love == "n":
           for x in range(1,999999,1): time.sleep(0.5554);print();print(Fore.RED + "FUCK YOU");stop.play()

else:
           print(Fore.YELLOW + "RETRY,VEGETABLE!")
           exc.play()
           time.sleep(1.1108)
           print(Fore.YELLOW + "Input yes!!!")
           print(Fore.YELLOW + intro)

#EXIT
input("PRESS ENTER TO EXIT")

if love == "yes" or love == "YES" or love == "1" or love == "y":
           print(Fore.GREEN + "BYE!")
           ding.play()
           time.sleep(0.5554)
           
elif love == "no" or love == "NO" or love == "2" or love == "n":
           print(Fore.RED + "SHIT!!")
           print(Fore.RED + "FUCK YOU");stop.play()

else:
           print(Fore.YELLOW + "NOOB!!")
           ding.play()
           
time.sleep(1.1108)
shutdown.play()
time.sleep(0.5554)
mixer.music.stop()
