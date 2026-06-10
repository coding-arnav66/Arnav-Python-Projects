import random, os, time, keyboard
print("Welcome to the city created by Saket.!")
print("You have 50 coins in default...")
print("Just follow the letter codes given after every option to select the option :)")         #intro
ddict = {"n": "north", "s": "south", "e": "east", "w": "west"}
coins = 50
qa_dict = {
    "Code to add a, b, c and store it in q": "q=a+b+c",
    "Code to multiply x and y and store it in p": "p=x*y",
    "Code to subtract b from a and store it in result": "result=a-b",
    "Code to divide m by n and store it in div": "div=m/n",
    "Code to find remainder of a divided by b and store it in r": f"r=a%b",
    "Code to raise x to power y and store it in ans": "ans=x**y",                            #dict for occupation coder
    "Code to store length of list l in n": "n=len(l)",
    "Code to append 10 to list l": "l.append(10)",
    "Code to sort list l": "l.sort()",
    "Code to reverse list l": "l.reverse()",
    "Code to store maximum of list l in m": "m=max(l)",
    "Code to store minimum of list l in m": "m=min(l)",
    "Code to open file data.txt in read mode and store it in f": "f=open('data.txt','r')",
    "Code to read all lines from file f and store them in lines": "lines=f.readlines()",
    "Code to close file f": "f.close()"
}
recipes = {
        "Veg Chowmein": "Noodles boiled, Cabbage shredded, Capsicum sliced, Soy sauce, Vinegar, Garlic minced",
    
    
        "Veg Manchurian (Dry)": "Cabbage grated, Carrot grated, Cornflour, Maida, Soy sauce, Chili sauce, Garlic finely chopped",
    
    
        "Chili Paneer (Dry)": "Paneer cubes, Capsicum diced, Onion diced, Soy sauce, Chili sauce, Cornflour, Garlic minced",
    
    
        "Fried Rice": "Cooked rice, Carrot finely chopped, Beans finely chopped, Soy sauce, Pepper powder, Spring onion",
    
    
        "Chili Potato": "Potato finger chips fried, Honey or Sugar, Chili sauce, Sesame seeds, Garlic minced, Soy sauce",
    
    
        "Hakka Noodles": "Noodles boiled, Onion sliced, Capsicum sliced, Soy sauce, Green chili sauce, Garlic minced",       #dict for occupation chef
    
    
        "Schezwan Rice": "Cooked rice, Schezwan sauce, Mixed veggies chopped, Garlic minced, Oil, Spring onion",
    
    
        "Paneer 65": "Paneer cubes, Curd, Red chili powder, Garam masala, Cornflour, Curry leaves",
    
    
        "Spring Roll (Easy Wrap)": "Tortilla or Readymade wrappers, Stir-fried veggies, Cornflour slurry, Oil for frying",
    
    
        "Garlic Noodles": "Noodles boiled, Garlic lots minced, Soy sauce, Chili flakes, Butter or Oil, Spring onion"
    }

def count(n):
    print("Starts in: ", end="")
    while n != 0:
        print(f"{n}...")
        time.sleep(1)
        n -= 1

def monster():
    global coins
    print("Spin the wheel to see who won...")
    input("Press anything to spin...")
    e = random.choice(["YOU WON!", "MONSTER WON!", "YOU WON!"])
    for i in range(random.randint(4, 14)):
        print("You won!")
        time.sleep(1)                                                         #monster game
        print("Monster won!")
        time.sleep(1)
    print(e)
    if e == "YOU WON!":
        coins += 25
        print(f"You got 25 coins! You now have {coins} coins.")
    else:
        print(f"You got 0 coins! You now have {coins} coins.")

def mining(tool, price, sf, nothingp):
    global coins
    if tool == sf:
        if price>coins:
            print(f"You took a loan of {price - coins} coins.")
        coins -= price
        print(f"You bought {sf} for {price} coins. You now have {coins} coins.")                           #mining
        ug = ["nothing"] * nothingp + ["diamond"]
        while True:
            userr = input("Press '7' to mine, or 'enter' to stop(5 coins will be deducted for each mine attemps...): ")
            if userr != "7":
                break
            coins -= 5
            result = random.choice(ug)
            if result == "nothing":
                print("You got nothing! You still have", coins, "coins.")
            else:
                print("You got a diamond worth 200 coins! Congrats!!!")
                coins += 200
                print(f"Total coins: {coins}")

while True:
    print(f"You have {coins} coins. Where do you want to go?\nNorth - n\nEast - e\nWest - w\nSouth - s")
    user = input("?: ").strip().lower()
    if user not in ddict:
        print("Invalid choice! Please type n, e, w, or s.")
        continue
    print(f"Welcome to {ddict[user]}")                                                          #message that tells about the location in which the user is...
    print(f"You {random.choice(['fell', 'jumped', 'walked'])} and saw a old {random.choice(['school', 'office', 'house', 'hospital', 'society', 'garden', 'hall'])} and decided to explore that...")
    a = random.choice(["Monster", "No monster", "No monster"])
    print(f"While exploring, you saw {a}")
    if a == "Monster":
        choice = input("Fight? - f\nNo fight(10 coins will be deducted) - nf::: ")
        if choice == "nf":
            print("Error 404, guts not found...")
            coins -= 10
            print(f"You lost 10 coins. You now have {coins} coins.")                          #choice to fight with monster
        elif choice == "f":
            monster()
    else: 
        o = random.randint(10, 50)
        print(f"You got random {o} coins as a gift from Saket!:)")
        coins += o
    if(random.choice([True, False])):
        time.sleep(3)
        print("You are now hungry! 10 coins to be deducted for food...")
        coins -= 10

    print("Now you see many types of occupation there...\nFarmer - f\nMiner - m\nCoder - c\nBusinessman - b\nHunter - h\nChef - ch")
    occ = input("Enter your choice: ")
    if "f" in occ:
        if(random.choice([True, False])):                                                            #chosing occupation by selecting a letter code
            time.sleep(3)
            print("You are now hungry! 10 coins to be deducted for food...")
            coins -= 10
        print("Welcome to farming!")                                                                         #logic for farmer
        seeds = int(input(f"You have {coins} coins. How many seeds do you want to buy? Cost of each is 10 coins: "))
        if (10*seeds)>coins:
            print(f"You took loan of {(10*seeds)-coins}...")
        print(f"You bought {seeds} seeds.")
        coins -= 10 * seeds
        print(f"You spent {10 * seeds} coins. You now have {coins} coins.")
        input("Press 'enter' to plant them and see result...")
        for i in range(seeds):
            print("Result in 3 seconds")
            count(3)
            safalta = random.choice(['yes', 'no', 'yes'])
            if safalta == 'yes':
                print(f"Success in seed no. {i + 1}")
                print("You earned 20 coins...")
                coins += 20
                print(f"You now have {coins} coins.")
            else:
                print("Crop failed! You earned nothing. You still have", coins, "coins.")
    elif "m" in occ:
        if(random.choice([True, False])):                                                             #logic for miner
            time.sleep(3)
            print("You are now hungry! 10 coins to be deducted for food...")
            coins -= 10
        print(f"You have {coins} coins. What do you want to purchase?\nHoe(25 coins) - he\nLittle axe(10 coins) - le\nBig pickaxe(45 coins) - be\nSpoon(5 coins) - sn\nHands(0 coins) - h")
        tool = input("Select any one: ")
        mining(tool, 25, "he", 19)
        mining(tool, 10, "le", 29)
        mining(tool, 45, "be", 9)
        mining(tool, 5, "sn", 39)
        mining(tool, 0, "h", 49)
    elif "c" in occ and "h" not in occ:
        if(random.choice([True, False])):
            time.sleep(3)
            print("You are now hungry! 10 coins to be deducted for food...")
            coins -= 10
        print("Welcome to coding...\nAnswer simple questions to earn 20 coins for each answer and loose 20 coins if you don\'t know the answer...")
        rounds = int(input(f"You have {coins} coins. How many rounds do you want?:"))
        
        for i in range(rounds):
            q = random.choice(list(qa_dict.keys()))
            a = qa_dict[q]
            print(f"The question is: {q}")
            userr = input("Enter the answer: ")
            user_ans = userr.replace(" ", "")
            if user_ans == a:
                print("Congats! Its correct...20 coins updated")
                coins += 20
            else:
                print("Answer is wrong...20 coins deducted")
                coins -= 20
        print(f"You have {coins} coins now...")
    elif "b" in occ:
        if(random.choice([True, False])):
            time.sleep(3)
            print("You are now hungry! 10 coins to be deducted for food...")
            coins -= 10
        print("Welcome businessman!")
        print("Invest your coins and have a equal chance to duble it or loose it...")                               #logic for businessman
        while True:
            uc = input(f"You have {coins} coins. How many coins do you want to invest? Enter amount or press \'stop\' to stop: ")
            if "stop" in uc:
                break
            ruc = int(uc)
            if ruc > coins:
                print("You dont have enough coins...")
                continue
            coins -= ruc
            print("Results in 5 sec...")
            count(5)
            if(random.choice([True, False])):
                print("You won!!!!!🤑🤑🤑")
                coins += 2*ruc
                print(f"Now you have {coins} coins...")
            else:
                print("Money wasted succesfully!! You got 0rs...")
    elif "h" in occ and "c" not in occ:
        if(random.choice([True, False])):
            time.sleep(3)
            print("You are now hungry! 10 coins to be deducted for food...")
            coins -= 10
        print("Welcome to hunting...")                                                                       #logic for hunter
        coins -= 50
        print(f"The cost of gun is 50 coins which has been deducted...Now, you have {coins} coins.")
        print("A random no of seconds will be given to you and you have to press \'h\' and \'enter\' after that period of time...")
        roundd = int(input("How many rounds do you want? For each round 5 coins will be deducted: "))
        print(roundd * 5, "coins deducted...")
        coins -= roundd * 5
        for i in range(roundd):
            a = random.randint(15, 25)
            time.sleep(2)
            print(f"You have to press the button in {a} seconds...")
            masti = input("Press anything to start: ")
            count(5)
            start = time.time()
            mastii = input(":::")
            end = time.time()
            tim = round(end - start, 2)
            print(f"You took {tim} sec...")
            if abs(tim-a) >2:
                print("You took more than 2 seconds... No coins earned...")
            else:
                print("You had a succesful shot on the animal... You earned 100 coins!")
                coins += 100
        print(f"Now you have {coins} coins...")
    elif("ch" in occ):
        if(random.choice([True, False])):
            time.sleep(3)
            print("You are now hungry! 10 coins to be deducted for food...")
            coins -= 10
        print("Welcome in cooking!")                                                                       #logic for chef
        roundss = int(input(f"You have {coins} coins. How many rounds do you want? 60 coins will be deducted for each: "))
        coins -= 60*roundss
        print("A dish will be shown, You have to type any three ingridients one by one... ")
        for i in range(roundss):
            print(f"Round {i+1} starting...")
            dish = random.choice(list(recipes.keys()))
            print(f"Dish is {dish}.")
            u1 = input("Enter 1st ingridient: ")
            u2 = input("Enter 2nd ingridient: ")
            u3 = input("Enter 3rd ingridient: ")
            print("Checking..")
            count(3)
            aa = recipes[dish]
            if(u1.lower() in aa.lower() and u2.lower() in aa.lower() and u3.lower() in aa.lower()):
                print("Congrats! You have succesfuly made and served the dish and earned 150 coins!")
                coins += 150
            else:
                print("There was a error in that... 0  coins earned...")
        print(f"You have {coins} coins now...")

    elif occ == "d":
            if random.choice([True, False]):
                time.sleep(3)
                print("You are now hungry! 10 coins to be deducted for food...")
                coins -= 10
                
            print("Welcome to Saket City General Hospital: Emergency Department")                                         #logic for doctor
            print("You are clocking in as the Chief Attending Physician. Lives are on the line.")
            
            rounds = int(input(f"You have {coins} coins. How many critical patients can you handle this shift?: "))
            
            medical_cases = [
                {
                    "desc": "An unconscious patient presents with pinpoint pupils, respiratory depression, and bradypnea (4 breaths/min).",
                    "opts": "Administer IV Naloxone - n\nInfuse IV Flumazenil - f\nIntubate and give Epinephrine - e",
                    "ans": "n"
                },
                {
                    "desc": "An EKG shows a complete lack of P-waves and an irregularly irregular QRS rhythm. The patient is dizzy.",
                    "opts": "Administer Amiodarone or beta-blockers for Atrial Fibrillation - a\nPush Adenosine rapidly for SVT - d\nApply immediate unsynchronized cardioversion (Defibrillation) - c",
                    "ans": "a"
                },
                {
                    "desc": "A patient presents with sudden unilateral facial droop, arm weakness, and slurred speech. Symptoms started 90 minutes ago. CT scan rules out hemorrhage.",
                    "opts": "Administer tissue Plasminogen Activator (tPA) thrombolytic therapy - t\nGive 325mg Aspirin and send home - a\nAdminister high-dose Heparin immediately - h",
                    "ans": "t"
                },
                {
                    "desc": "An elderly patient with an infection becomes confused, hypotensive (BP 80/40), and has a lactic acid level of 4.2 mmol/L.",
                    "opts": "Initiate aggressive IV crystalloid fluid resuscitation and broad-spectrum antibiotics for Sepsis - s\nGive oral acetaminophen and monitor temperature - t\nOrder a fasting blood glucose test - g",
                    "ans": "s"
                },
                {
                    "desc": "A patient experiences sudden, severe shortness of breath after a 14-hour flight. Plural chest pain is sharp. D-dimer test is highly elevated.",
                    "opts": "Start therapeutic Anticoagulation (Heparin) for a Pulmonary Embolism - a\nAdminister Albuterol nebulizer for acute Asthma - b\nGive Nitroglycerin sublingually - n",
                    "ans": "a"
                },
                {
                    "desc": "A patient presents with crushing substernal chest pain radiating to the left jaw. EKG confirms a ST-elevation myocardial infarction (STEMI).",
                    "opts": "Activate the Cardiac Catheterization Lab for immediate PCI (Angioplasty) - c\nOrder a GI cocktail for suspected acid reflux - g\nAdminister high-dose NSAIDs and wait - w",
                    "ans": "c"
                },
                {
                    "desc": "A diabetic patient is found sweaty, shaking, and confused. A fingerstick glucose test reads 38 mg/dL.",
                    "opts": "Administer IV Dextrose (D50) or intramuscular Glucagon - d\nInject 10 units of rapid-acting Insulin - i\nAdminister Metformin orally - m",
                    "ans": "d"
                },
                {
                    "desc": "An unrestrained driver in a car crash has absent breath sounds on the left side, tracheal deviation to the right, and severe hypoxia.",
                    "opts": "Perform immediate Needle Decompression in the 2nd intercostal space - n\nOrder an emergency stat MRI scan - m\nUse an incentive spirometer to expand the lungs - l",
                    "ans": "n"
                },
                {
                    "desc": "A patient presents with a rigid, board-like abdomen, extreme rebound tenderness, and free air under the diaphragm on an X-ray.",
                    "opts": "Call General Surgery for an immediate laparotomy for gastrointestinal perforation - s\nAdminister Laxatives for severe fecal impaction - l\nPrescribe Antacids and clear liquid diet - a",
                    "ans": "s"
                },
                {
                    "desc": "A known diabetic presents with deep, rapid breathing (Kussmaul), fruity breath odor, a blood glucose of 450 mg/dL, and arterial pH of 7.15.",
                    "opts": "Initiate IV Regular Insulin infusion and aggressive fluid/electrolyte replacement - i\nAdminister Glucagon immediately - g\nGive a continuous breathing treatment of Albuterol - b",
                    "ans": "i"
                },
                {
                    "desc": "A patient presents with high fever, stiff neck (nuchal rigidity), photophobia, and a positive Brudzinski's sign.",
                    "opts": "Perform a Lumbar Puncture and start empiric IV Antibiotics/Corticosteroids - l\nOrder a cervical spine X-ray to check for a pinched nerve - c\nPrescribe muscle relaxants and bed rest - r",
                    "ans": "l"
                },
                {
                    "desc": "A patient stung by a wasp presents with diffuse urticaria (hives), stridor, wheezing, and a blood pressure of 75/40.",
                    "opts": "Inject Intramuscular Epinephrine (1:1000) in the lateral thigh immediately - e\nGive oral Diphenhydramine (Benadryl) and wait 1 hour - b\nApply hydrocortisone cream to the sting site - c",
                    "ans": "e"
                },
                {
                    "desc": "A chronic alcoholic presenting with persistent vomiting becomes suddenly confused, shows ataxia, and has horizontal nystagmus (Wernicke's Encephalopathy).",
                    "opts": "Administer high-dose IV Thiamine (Vitamin B1) before any glucose - t\nInfuse D5W fluid rapidly - d\nAdminister Phenytoin to prevent seizures - p",
                    "ans": "t"
                },
                {
                    "desc": "A child is brought in after accidentally swallowing an unknown quantity of a family member's iron supplements 1 hour ago. They are vomiting blood.",
                    "opts": "Initiate chelation therapy with Deferoxamine - d\nAdminister Activated Charcoal - a\nPerform immediate gastric lavage with hydrogen peroxide - h",
                    "ans": "d"
                },
                {
                    "desc": "A pregnant woman at 34 weeks gestation presents with a blood pressure of 170/110, severe headache, blurred vision, and hyperreflexia.",
                    "opts": "Administer IV Magnesium Sulfate for seizure prophylaxis and manage delivery - m\nPrescribe low-dose Lisinopril and tell her to rest - l\nGive high-dose Furosemide (Lasix) IV - f",
                    "ans": "m"
                },
                {
                    "desc": "A patient experiences a severe generalized tonic-clonic seizure that has lasted for 7 minutes without stopping (Status Epilepticus).",
                    "opts": "Administer IV Lorazepam (Ativan) or Diazepam immediately - l\nStart a loading dose of oral Levetiracetam (Keppra) - k\nPlace a padded tongue blade in the patient's mouth - b",
                    "ans": "l"
                },
                {
                    "desc": "A patient presents with severe bradycardia (HR 32 bpm), hypotension, and a history of accidental double-dose beta-blocker ingestion.",
                    "opts": "Administer IV Glucagon as an antidote - g\nGive high-dose Amiodarone IV - a\nInfuse Naloxone - n",
                    "ans": "g"
                },
                {
                    "desc": "A patient presents with sharp chest pain that improves when sitting forward and worsening when lying flat. EKG shows diffuse ST-elevation and PR-depression.",
                    "opts": "Treat with high-dose NSAIDs and Colchicine for acute Pericarditis - c\nAdminister tPA for acute myocardial infarction - t\nHeparinization for an unstable aortic dissection - h",
                    "ans": "c"
                },
                {
                    "desc": "A patient undergoing chemotherapy presents with a temperature of 101.3 F (38.5 C) and an Absolute Neutrophil Count (ANC) of 350 cells/microL.",
                    "opts": "Diagnose Neutropenic Fever and immediately start broad-spectrum antipseudomonal IV Antibiotics - e\nAdvise outpatient observation and oral acetaminophen - o\nAdminister a live virus vaccine to boost immunity - v",
                    "ans": "e"
                },
                {
                    "desc": "A psychiatric patient taking Haloperidol presents with a fever of 104 F, severe muscle rigidity ('lead-pipe'), autonomic instability, and altered mental status.",
                    "opts": "Stop the antipsychotic and administer Dantrolene for Neuroleptic Malignant Syndrome - d\nTreat with IV Flumazenil - f\nGive high-dose Haloperidol to stabilize the psychosis - h",
                    "ans": "d"
                }
            ]

            if rounds > len(medical_cases):
                rounds = len(medical_cases)
                print(f"We only have {rounds} critical cases available in triage right now!")

            random.shuffle(medical_cases)

            for i in range(rounds):
                print(f"\nEMERGENCY CASE #{i+1}")
                case = medical_cases[i]
                print(case["desc"])
                print("\nTREATMENT PROTOCOLS:")
                print(case["opts"])
                
                treatment = input("\nEnter code letter for immediate intervention: ").strip().lower()
                
                if treatment == case["ans"]:
                    print("Excellent triage! The patient is stabilized. You earned 200 coins!")
                    coins += 200
                else:
                    print("Incorrect medical intervention! Malpractice lawsuit filed. You all coins are deducted and only 20 coins are left with you.")
                    coins -= (coins - 20)
                    
            print(f"\nYour shift has ended. You now have {coins} coins.")
    print("To leave game - l; continue - c")                                   #cinfirming if user wants to leave
    userrr = input(":::")
    if "l" in userrr:
        break
namee = input("Enter your name: ")
print("Generating certificate...")                                             #generating a thank you certificate as well as certificate for appreciation
time.sleep(5)
from fpdf import FPDF
import qrcode
data = f"{namee} has collected {coins} coins in the ultimate city game...\nThank You for playing the game! :) "
qr = qrcode.make(data)
qr.save("qr.png")
# Create PDF object
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 24)
pdf.cell(200, 20, "Certificate of Appreciation", ln=True, align="C")

# Subtitle
pdf.set_font("Arial", '', 16)
pdf.cell(200, 10, "Presented to", ln=True, align="C")

# Player name
name = namee   # you can replace this with input()
pdf.set_font("Arial", 'B', 20)
pdf.cell(200, 20, name, ln=True, align="C")

# Body text
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10,
    f"This certificate is proudly awarded to {name} "
    "for successfully completing the City Game challenge "
    f"with dedication and enthusiasm, collecting {coins} coins in total!!!"
)
pdf.image("qr.png", x=80, y=150, w=50, h=50)                                                         #including qr code for authentication
# Footer
pdf.set_font("Arial", 'I', 10)
pdf.cell(0, 10, "Signed by: MR. A Saket", ln=True, align="R")
pdf.set_font("Arial", 'I', 10)
pdf.cell(0, 10, "Here is your QR code:", ln=True, align="C")

# Save PDF
pdf.output(f"certificate_for_{namee}.pdf")                                                        #saving the pdf

print("Certificate generated...! It is saved in the same folder...")















