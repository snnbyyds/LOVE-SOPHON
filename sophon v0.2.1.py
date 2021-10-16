#PREP
import time   #time                      
from pygame import mixer   #sound
from colorama import Fore,Back,Style,init  #colour
init(autoreset = True)    #color auto reset

#AUDIO
mixer.init()
#unlock=() not used
shutdown=("Windows Shutdown.wav")
exc=("Windows Exclamation.wav")
ding=("Windows Ding.wav")
stop=("Windows Critical Stop.wav")

#ABOUT "love Sophon" programme
print(Fore.YELLOW + "============================ABOUT=====================================")
ver=str("v0.2.0");author=str("sn");intro=str("SOPHON=GOD! I'll FUCK anyone who doesn't like Sophon")
print(Fore.RED + "LOVE SOPHON",ver,Fore.RED + ".Unstable")
time.sleep(0.2)
print(Fore.GREEN + "author:",author)
time.sleep(0.2)
mixer.music.load(exc);mixer.music.play()
print(Fore.RED + intro)
print()

#CHANGELOG
print(Fore.GREEN + "============================CHANGELOG=================================")
print("1.YOU CAN USE yes OR no to answer")
print("2.REMOVED A SOUND EFFECT TO AVOID CRASH") #bug
print("3.COLOUR ADDED")
print()

#PAUSE
time.sleep(2)

#START
line=str(Fore.GREEN + "===========================START!===================================")
mixer.music.load(ding);mixer.music.play()
print(line)
time.sleep(1)
print()
print(Fore.GREEN + "Do you",Fore.RED + "love Sophon? ")
time.sleep(1)
love=str(input("Input:"))

if love == "yes" or love == "YES":
           print(Fore.GREEN + "GREAT")
           mixer.music.load(ding);mixer.music.play()
           time.sleep(0.5)
           print(Fore.GREEN + "GOD SOPHON!!")
           mixer.music.load(ding)
           mixer.music.play()

elif love == "no" or love == "NO":
           for x in range(1,999999,1): time.sleep(0.5);print();mixer.music.load(stop);print(Fore.RED + "FUCK YOU");mixer.music.play()

else:
           print(Fore.YELLOW + "RETRY,VEGETABLE!")
           mixer.music.load(ding)
           mixer.music.play()
           time.sleep(1)
           print(Fore.YELLOW + "Input yes!!!")
           print(Fore.YELLOW + intro)

#EXIT
input("PRESS ENTER TO EXIT")
print(Fore.GREEN + "BYE!")
time.sleep(1)
mixer.music.load(shutdown);mixer.music.play()
time.sleep(0.8)
mixer.music.stop()
