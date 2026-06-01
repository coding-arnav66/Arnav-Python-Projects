import random
import  speech_recognition as sr, time, os
import pygame
from gtts import gTTS
from mutagen.mp3 import MP3
from io import BytesIO
mode = input("Select mode:\n1. Repeat mode - a\n2. Sound effects - b\n3. Random answers of question - c: ")
if("a" in mode.lower()):
    pygame.mixer.init()

    # Intro speech
    tts = gTTS("This is repeat mode... Say something!", lang="en", slow=False)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    pygame.mixer.music.load(mp3_fp, "mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    try:
        while(True):
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Say something!")
                    audio = r.listen(source, timeout = 7)
                user = r.recognize_google(audio)
                print(user)
                tts = gTTS(user, lang="en", slow=True)
                a = random.randint(100000000, 999999999)

                mp3_fp = BytesIO()
                tts.write_to_fp(mp3_fp)

                # rewind buffer and load into pygame
                mp3_fp.seek(0)
                pygame.mixer.music.load(mp3_fp, "mp3")
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    time.sleep(0.1)
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
    except Exception as e:
         print(e, "Programme ended!")
def se(arg):
    if(arg in user):
        os.system(f"start {arg}.mp3")
        audio = MP3(f"{arg}.mp3")
        time.sleep(audio.info.length + 1.5)
if("b" in mode.lower()):
    print("Wait!")
    pygame.mixer.init()
    tts = gTTS("This is sound effect mode...You can say laugh, cry, horror, applause, animals, or even random to play them. Please say properly and 2-3 times each for better recognition, or use them in a sentence...", lang="en", slow=False)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    pygame.mixer.music.load(mp3_fp, "mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    try:
        while(True):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source, timeout = 7)
            user = r.recognize_google(audio)
            print(user)
            se("cry")
            se("laugh")
            se("horror")
            se("applause")
            se("animal")
            if("random" in user.lower()):
                listt = random.choice(["cry", "laugh", "horror", "applause", "animal"])
                os.system(f"start {listt}.mp3")
                audio = MP3(f"{listt}.mp3")
                time.sleep(audio.info.length + 1.5)
    except Exception as u:
        print(u, "Programme ended!")


if("c" in mode.lower()):
    print("Wait!")
    pygame.mixer.init()
    tts = gTTS("This is q n a mode...You can ask questions and get a random answer of that!", lang="en", slow=False)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    pygame.mixer.music.load(mp3_fp, "mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    try:
        while True:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source, timeout = 7)
            user = r.recognize_google(audio)
            print(user)
            time.sleep(0.5)
            ans = random.choice(['yes','yez', 'no','no', 'probably','probably', 'i dont want to talk about that', 'i dont know', 'i think this shouldn\'t be answered'])
            pygame.mixer.init()
            tts = gTTS(ans, lang="en", slow=False)
            mp3_fp = BytesIO()
            tts.write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            pygame.mixer.music.load(mp3_fp, "mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            time.sleep(5)
    except Exception as r:
        print(r, "Programme ended!")
        



     
            
            
