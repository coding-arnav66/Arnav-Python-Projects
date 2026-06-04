import webbrowser, pyautogui, time, keyboard
print("Welcome to AI clash. Ask a question and get the answer with all AI chatbox...press \'%\' to move to another AI...")

user = input("User: ")                                                     #asking from the user
print("Process starting...")
def search(url, so):
    webbrowser.open(url)
    if(so == "yes"):
        time.sleep(7)
        pyautogui.press("escape")                                      
        pyautogui.typewrite(user)
        time.sleep(2)
        pyautogui.press("enter")                                        #defining ai searching
    else:
        time.sleep(4)
        pyautogui.typewrite(user)
        time.sleep(3)
        pyautogui.press("enter")


search("https://chatgpt.com", "yes")                                 #searching on chat gpt for the user asked question...

while True:
    if keyboard.is_pressed('%'):                                     #searching for wakening letter - %, to move on
        webbrowser.open("https://copilot.microsoft.com")             #searching on chat gpt for the user asked question...
        time.sleep(5)
        pyautogui.typewrite(user)
        time.sleep(2)
        pyautogui.press("enter")
        break
while True:
    if keyboard.is_pressed('%'):                                   #wakening letter search for next ai
        search("https://duck.ai", "no")                            #asking duck ai as our last ai...
                                                                   #claude was not included because it is facing server problems as per 4 june...
        break
            
