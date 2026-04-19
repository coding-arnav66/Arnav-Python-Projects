import time
from plyer import notification

q = int(input("Enter the length of time intervals you want between the notifications: "))
print(f"Water remainder will pop out in every {q} seconds...")

def h2o_remainder():
    while True:
        notification.notify(
            title = "Hey! Drink Water 💧",
            message = "You've been studying hard. Take a sip of water to stay hydrated!",
            app_icon = None, # You can add a .ico file path here later
            timeout = 10 # The notification stays for 10 seconds
        )
        time.sleep(q)

if __name__ == "__main__":
    h2o_remainder()        