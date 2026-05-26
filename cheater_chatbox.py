import webbrowser, pyautogui, speech_recognition as sr, time, pyttsx3,os

pt = []

try:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source, timeout = 15)
    user = r.recognize_google(audio)
    print(user)
    time.sleep(1)
    webbrowser.open(f"https://chat.openai.com")
    time.sleep(7)
    pyautogui.press('escape')
    pyautogui.typewrite(f"In my conversation with my friend,the previous lines he said was/were- {pt}(ignore if empty), now he is saying {user}.. reply what should i say in one line, whithout any other texts by learning from past texts...")
    pyautogui.press("enter")
    pt.append(user)  

    while True:
        time.sleep(6)
        
        engine = pyttsx3.init()
        engine.setProperty('rate', 179)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)  # or Zira for female
        engine.say("Continue... I am listening. you can continue you conversations and the process will continue in the background. Say quickly after the ai replies. Watch the microphone icon in your taskbar. when it activates, talk! ")
        engine.runAndWait()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source, timeout = 15)
        user = r.recognize_google(audio)
        pyautogui.typewrite(f"In my conversation with my friend,the previous lines he said was/were- {pt}(ignore if empty), now he is saying {user}.. reply what should i say in one line, whithout any other texts by learning from past texts...")
        pyautogui.press("enter")
        time.sleep(3)
        pt.append(user)  
        os.system('cls')      
except Exception as e:
    from gtts import gTTS
    import os

    # Create speech
    tts = gTTS("Your chat has ended either because of error or you might have stopped speaking...", lang="en", slow=False)

    # Save to file
    tts.save("hello.mp3")

    # Play the file
    os.system("start hello.mp3")  


