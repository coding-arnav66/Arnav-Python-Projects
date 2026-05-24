import random
import time, os




g1 = [
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M',
'N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
'0','1','2','3','4','5','6','7','8','9',
'!','"','#','$','%','&',"'",'(',')','*','+',
',','-','.','/',':',';','<','=','>','?','@',
'[','\\',']','^','_','`','{','|','}','~',
' '
]
subjects = ["The cat", "A student", "My friend", "The computer", "An astronaut"]
verbs = ["runs", "jumps", "codes", "explores", "sings"]
objects = ["in the park", "over the moon", "Python scripts", "new planets", "loudly"]
points = {"p1" : 0,
    "p2" : 0
}














def keygame():
    for i in range(2):
        print("Game for player:", i+1)
        char = random.choice(g1)
        print("round starting...")
        time.sleep(10)
        print("In 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        start = time.time()
        user = input(f"Time starts!\nThe character: {char}...::::")
        end = time.time()
        if(user == char):
            res = "correct"
        else:
            res = "incorrect"
        tim = round(end - start, 2)
        if(tim < 2):
            pt = 10
        elif(tim>=2 and tim <=3 ):
            pt = 8
        else:
            pt = 5





        points[f"p{i+1}"] += pt
        print(F"You typed {char} in a {res} way.")
        print("Your points are updated!")

# print("Game 1: Computer will show you random character from keyboard.\nWhoever types it correct and presses enter in shortest time, wins!\nStarting in 5 seconds... ")
# time.sleep(5)
# keygame()
def dice():
    for i in range(2):
        mast = input("Type anything to start: ")
        score = 0
        amt = 0
        print("For new player:")
        while(score <= 30):
            user = input("Type roll to roll the dice...")
            d = random.randint(1, 6)
            print(f"Dice stopped at {d}")
            score += d
            amt += 1
        print("Your dice reached 30!")
        if(amt > 10):
            points[f"p{i+1}"] += 2
        if(amt <= 10 and amt > 8):
            points[f"p{i+1}"] += 8
        if(amt == 6 or amt == 5 or amt == 7 or amt == 8):
            points[f"p{i+1}"] += 10
        print("Your points are updated!")
# dice()
# print(points)
def mat():
    
    for i in range(2):
        print("For new player:")
        masti = input("Type anything to start: ")
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = random.randint(1, 20)
        d = random.randint(1, 20)
        f = random.randint(1, 15)
        g = random.randint(1, 10)
        print("Starts in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        start1 = time.time()
        user = int(input(f"{a} + {b} = "))
        end1 = time.time()
        if(user == a+b):
            x = "correct"
            print("Answer is correct!")
        else:
            x = "incorrect"
            print("Answer is incorrect!")
        print("Next in 5 seconds...")
        time.sleep(5.9)
        start2 = time.time()
        user2 = int(input(f"{c} + {d} = "))
        end2 = time.time()
        if(user2 == c+d):
            y = "correct"
            print("Answer is correct!")
        else:
            y = "incorrect"
            print("Answer is incorrect!")
        print("Next in 5 seconds...")
        time.sleep(5.9)
        start3 = time.time()
        user3 = int(input(f"{f} x {g} = "))
        end3 = time.time()
        if(user3 == f*g):
            z = "correct"
            print("Answer is correct!")
        else:
            z = "incorrect"
            print("Answer is incorrect!")
        print("Points updated...")
        time1 = round(end1 - start1, 2)
        time2 = round(end2 - start2, 2)
        time3 = round(end3 - start3, 2)
        pts = 0

        if(x == "correct"):
            if(time1 <= 10):
                pts += 10
            elif(time1 > 10):
                pts += 5
        if(y == "correct"):
            if(time2 <=10):
                pts += 10
            elif(time2 > 10):
                pts += 5
        if(z == "correct"):
            if(time3 <=10):
                pts += 10
            elif(time3 > 10):
                pts += 5
        points[f"p{i+1}"] += pts
# mat()
# print(points)

def memory():
    for i in range(2):
        print("For new player...")
        masti = input("Type anything to start...")
        num = random.randint(100000000, 999999999)
        print("Remember the number...")
        print("Starting in 3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print(f"Remember {num}")
        time.sleep(12)
        os.system('cls')
        ans = int(input("Enter no: "))
        if(ans == num):
            print("Its correct! Congrats!")
            points[f"p{i+1}"] += 10
        else:
            print("Answer is incorrect!")
        print("Points updated...")
# memory()

def typeing():
    for i in range(2):
        print("Round for new player")
        sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}"
        masti = input("Type anything to start: ")
        print("Showing sentence in 3 seconds...Remember it...")
        time.sleep(4)
        print(f"Remember the sentence:", sentence)
        time.sleep(7)
        os.system('cls')
        print("After 3 seconds, type it as fast as u can...")
        time.sleep(4)
        start = time.time()
        user = input("Type it: ")
        end = time.time()
        timee = round(end - start, 2)
        if(sentence.lower() == user.lower()):
            print("You typed it correctly!")
            if(timee <=7):
                points[f"p{i+1}"] += 10
            elif(timee > 7):
                 points[f"p{i+1}"] += 8
        else:
            print("You typed it incorrectly!")
        print("Points updated...")
# typeing()
print("Welcome to 2-player olympics!")
print("You will play games like-\nKeyboard reaction time challange.\nDice race.\nMath race.\nMemory game.\nSpeed typing.")
print("Be ready with your opponent.")
masti = input("Type anything to start the olympics: ")
os.system('cls')
print("Game 1: Computer will show you random character from keyboard.\nWhoever types it correct and presses enter in shortest time, wins!\nStarting in 5 seconds... ")
time.sleep(5)
keygame()
time.sleep(2)
os.system('cls')
print("Game 2: Roll the dice and reach 30 in shortest number of chance...")
dice()
time.sleep(2)
os.system('cls')
print("Game 3: Solve the math equations in shortest period of time...")
mat()
time.sleep(2)
os.system('cls')
print("Game 4: Remember the 9-digit no and type it in the shortest period of time...")
memory()
time.sleep(2)
os.system('cls')
print("The last game: Type the given sentence in the shortest period of time...")
typeing()
time.sleep(2)
os.system('cls')

print("Note that distribution of points is very logical. Here is the points table of player 1 and player 2:\n", points)
if(points['p1'] > points['p2']):
    print("Player 1 won the game!")
else:
    print("Player 2 won the game!")





    
                




