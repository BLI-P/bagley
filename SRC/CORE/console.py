# This file contains all console based operation of the Bagley A.I
#  Author : RETR0
# CodeXno : 1.0 (sigma)

import playsound
from core import speak
from colorama import Fore
import gtts
import requests

def internetConnector(url='http://www.torr.pages.dev/', timeout = 5):
    try:
        socketConnection = requests.head(url, timeout = timeout)
        print(Fore.GREEN + "Initalization completed.", end = "")
        print(Fore.RESET + "", end = "")
        speak("Completing the final initalization..")
        return True
    except requests.ConnectionError:
        print(Fore.RED + "Initalization incompleted.", end = "")
        print(Fore.RESET + "", end = "")
        speak("The initalization couldn't be completed...")
    return False

def speak(command):
    bagVoice = gTTS(text= command, lang= "en", slow=False)
    bagVoice.save("audio.mp3")
    playsound.playsound("audio.mp3")
    
    
    
    







