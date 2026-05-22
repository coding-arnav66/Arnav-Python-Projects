
import random


not_costly = {
    "Pen": random.randint(5, 50),
    "Notebook": random.randint(20, 200),
    "Book": random.randint(100, 800),
    "Shoes": random.randint(1000, 3000),
    "Wallet": random.randint(500, 1000),
    "Bag": random.randint(300, 2500),
    "Watch": random.randint(500, 5000),
    "Remote": random.randint(200, 800),
    "Chair": random.randint(500, 5000),
    "Mattress": random.randint(2000, 3000),
    "Pillow": random.randint(200, 1000),
    "Blanket": random.randint(500, 800),
    "Curtain": random.randint(300, 1000),
    "Lamp": random.randint(800, 2000),
    "Clock": random.randint(200, 1500),
    "Fan": random.randint(1000, 5000),
    "Kettle": random.randint(500, 3000),
    "Toaster": random.randint(500, 3000),
    "Cooker": random.randint(3000, 8000),
    "Pan": random.randint(300, 2000),
    "Plate": random.randint(50, 500),
    "Glass": random.randint(50, 500),
    "Cup": random.randint(50, 500),
    "Spoon": random.randint(10, 200),
    "Fork": random.randint(10, 200),
    "Knife": random.randint(100, 1000),
    "Bottle": random.randint(500, 1000),
    "Box": random.randint(100, 1000),
    "Mirror": random.randint(500, 1800),
    "Brush": random.randint(50, 1800),
    "Soap": random.randint(10, 100),
    "Carpet": random.randint(1000, 6000),     
    "Table": random.randint(1000, 6000) 
}


costly = {
    "Phone": random.randint(10000, 150000),
    "Laptop": random.randint(20000, 200000),
    "TV": random.randint(10000, 80000),
    "Sofa": random.randint(10000, 40000),
    "Bed": random.randint(5000, 50000),
    "Fridge": random.randint(10000, 60000),
    "Microwave": random.randint(10000, 20000),   
    "Stove": random.randint(2000, 15000),       
    
}



rounds = int(input("How many rounds do you want: "))
players = int(input("How many player(s) are playing?: "))
result = {}


def guess_price(hmr, hmp):
    for p in range(hmp):    
        print("Round for new player: ")
        a = 0
        for r in range(hmr):
            e = random.choice([costly, not_costly])
            klist = list(e.keys())
            product = random.choice(klist)
            if(product in list(not_costly.keys())):
                print("Product comes in \'not expensive\' category.")
            else:
                print("Product comes in \'expensive\' category.")
            print(f"Product is: {product}")
            gp = int(input("Enter guess: "))
            ap = e[product]
            print("Actual price is:", ap)
            difference = abs(ap - gp)
            print("Different between actual price and guessed price is:", difference)
            a += difference
        result.update({f"player{p+1}": a})
    print("Remember who played first? Here is the score of all players:", result, "\nThe one with lowest difference wins!")



if (players > 1):
    guess_price(rounds, players)
if (players == 1):
    csc = 0
    usc = 0
    dict1 = {}
    for t in range(rounds):
        e = random.choice([costly, not_costly])
        klist = list(e.keys())
        product = random.choice(klist)
        ap = e[product]
        if(product in list(not_costly.keys())):
            print("Product comes in \'not expensive\' category.")
        else:
            print("Product comes in \'expensive\' category.")
        print("Product:", product)

        ug = int(input("Enter your guess: "))
        if(product in list(not_costly.keys())):
            cguess = random.randint(10, 5000)
        else:
            cguess = random.randint(5000, 50000)
        print("Computer guessed:", cguess)
        cdif = abs(cguess - ap)
        csc += cdif
        udif = abs(ug - ap)
        usc += udif
        print("Actual price:", ap)
    print("The one with lowest difference wins!")
    dict1.update({"Computer": csc})
    dict1.update({"User": usc})


    print("Score:", dict1)
    

            

        




