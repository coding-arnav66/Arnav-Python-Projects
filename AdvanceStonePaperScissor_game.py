import random, os
name = input("What is your name?: ")                                                 #asking for name to store data in a personal txt file
def game_before_learning():
    f = open(f"{name}'s_data.txt", "a")
    for i in range(10):
        while True:
            comp = random.choice(["1", "2" ,"3"])
            youstr = input("enter your choice(stone/paper/scissor): ")             #if its a new user, this is the game which will note the moves in the txt file in form of 1, 2 and 3
            youdict = {
                        "stone" : "1",
                    "paper" : "2",
                        "scissor" : "3"
            }
            if youstr not in youdict:
                print("Invalid choice...Try again!")
                continue
            else:
                you = youdict[youstr]
                if(you == comp):
                    print("computer chose the same, \n draw")
                else:
                    if(comp == "1" and you == "2"):
                        print("computer chose stone\nyou win ")
                    elif(comp == "1" and you == "3"):
                        print("computer chose stone\nyou lose")
                    elif(comp == "2" and you == "1"):
                        print("computer chose paper\nyou lose")
                    elif(comp == "2" and you == "3"):
                        print("computer chose paper\nyou win")
                    elif(comp == "3" and you == "1"):
                        print("computer chose scissor\nyou win")
                    elif(comp =="3" and you == "2"):
                        print("computer chose scissor\nyou lose")
                f.write(you)                                                    #writing the move in the file
                break
    f.close()
def game_after_learning():
    with open(f"{name}'s_data.txt") as r:                                       #if its a old user, or new user has completed the first part, this will take place next 
        data = r.read()
    data_for_learning = list(data)
    pattern = {                                                                 #noting the pattern so that after a move, which move is played more frequently can be noted down
        "1" : {"1" : 0, "2" : 0, "3" : 0},
        "2" : {"1" : 0, "2" : 0, "3" : 0},
        "3" : {"1" : 0, "2" : 0, "3" : 0}
    }
    win = {                                                                     #dict to know that which move is used to defeat which move
        "1" : "2",
        "2" : "3",
        "3" : "1"
    }
    q = open(f"{name}'s_data.txt", "a")
    while True:                                                                #to update 'pattern(dict)' according to user's data
        for a in range(len(data_for_learning)-1):
            current_move = data_for_learning[a]
            next_move = data_for_learning[a+1]
            pattern[current_move][next_move] += 1
        youstr = input("enter your choice(stone/paper/scissor): ")
        prediction = {                                                          #prediction based on 'pattern(dict)' using max and get func
        "1" : max(pattern["1"], key=pattern["1"].get),
        "2" : max(pattern["2"], key=pattern["2"].get),
        "3" : max(pattern["3"], key=pattern["3"].get)
        }
        last_move = data_for_learning[-1]                                       #to see what user has played latest and predict the next move's defeating move
        comp = win[prediction[last_move]]                                       #computer's prediction(made before user enters the input)
        youdict = {
                "stone" : "1",
                "paper" : "2",
                "scissor" : "3"
        }
        if youstr not in youdict:
            print("Invalid choice...Try again!")
            continue
        else:
            you = youdict[youstr]
            q.write(you)
            data_for_learning.append(you)
            if(you == comp):
                print("computer chose the same, \n draw")
            else:
                if(comp == "1" and you == "2"):
                    print("computer chose stone\nyou win ")
                elif(comp == "1" and you == "3"):
                    print("computer chose stone\nyou lose")
                elif(comp == "2" and you == "1"):
                    print("computer chose paper\nyou lose")
                elif(comp == "2" and you == "3"):
                    print("computer chose paper\nyou win")
                elif(comp == "3" and you == "1"):
                    print("computer chose scissor\nyou win")
                elif(comp =="3" and you == "2"):
                    print("computer chose scissor\nyou lose")
if os.path.exists(f"{name}'s_data.txt"):                                   #if old user, directly start game after learning
    print(f"Welcome back {name}, Your past data imported!")
    game_after_learning()
else:                                                                      #else, execute both game which were before learning and after learning
    print(f"Welcome {name}!")
    game_before_learning()
    game_after_learning()
