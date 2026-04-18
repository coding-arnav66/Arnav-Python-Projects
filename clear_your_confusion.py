import random


print ("welcome to clear your confusion \ntype your options one by one and type \"done\" when completed")

opt = []
while True:
    user = input("enter your choice: ")
    opt.append(user)

    if (user.lower() == "done"):
        break

    a = random.choice(opt)
print ("the selected one is:", a)