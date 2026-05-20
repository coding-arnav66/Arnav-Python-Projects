import time
from plyer import notification

q = int(input("Enter the length of time intervals you want between the notifications(in seconds): "))    #taking time interval as a input
print(f"Water remainder will pop out in every {q} seconds...")


while True:
    notification.notify(
        title = "Hey! Drink Water 💧",
        message = "You've been working hard. Take a sip of water to stay hydrated :)",              #the message
        app_icon = None, 
        timeout = 20
    )
    time.sleep(q)
    
