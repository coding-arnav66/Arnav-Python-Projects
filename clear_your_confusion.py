import random


print ("welcome to clear your confusion \ntype your options one by one and type \"done\" when completed")

opt = []
while True:
    user = input("enter your choice: ")
    opt.append(user)                                               #adding the inputs given by user in a list until user types done

    if (user.lower() == "done"):
        break

    a = random.choice(opt)
print ("the selected one is:", a)                                 #choosing a random stuff and printing it
