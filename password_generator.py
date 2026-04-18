import random


print ("Created by Arnav Saket \n not so efficient password generator :(")
y  = input("enter your name: ")
z = int(input("enter the length of password(4/6/8/10/12): "))
x = input("enter the format of password(password with only numbers/password with name): ")
ao = random.randint(0, 9)
bo = random.randint(10, 99)
co = random.randint(100, 999)
do = random.randint(1000, 9999)
eo = random.randint(100000, 999999)
a = str(ao)
b = str(bo)
c = str(co)
d = str(do)
e = str(eo)
j = random.choice(["@", "#", "$"])
h = len(y)

if(z == 4 and  "name" in x.lower()):
    i = y[0 : 3]
    print ("Your password is: ", a + i)

elif(z == 4 and "numb" in x.lower()):
    print ("your password is: ", d)



elif(z == 6 and  "name" in x.lower()):
    if(h <=5):
        aa = y[1:4]
        print("password is: ", a + aa + j)
    elif( h > 5):
        fa = y[0:4]
        print("your password is: ", a + fa + j)

elif(z == 6 and "numb" in x.lower()):
    
    print ("your password is: ", e)

elif(z == 8 and  "name" in x.lower()):
    if(h <= 5):
        ww = y[0:4]
        print ("your password is: ",d + ww + j )
    elif(h > 5):
        qq = y[0:5]
        print("your password is: ",c + qq + j )
    

elif(z == 10 and  "name" in x.lower()):
    if(h <= 5):
        ww = y[0:5]
        print ("your password is: ",d + ww + j )
    elif(h > 5):
        qq = y[0:6]
        print("your password is: ",c + qq + j )

elif(z == 12 and  "name" in x.lower()):
    if(h <= 5):
        ww = y[0:5]
        print ("your password is: ",e + ww + j )
    elif(h > 5):
        qq = y[0:7]
        print("your password is: ",d + qq + j )


elif (z == 8 and "numb" in x.lower()):
    print (" who generates that long numbers u dumb! \n close your eyes and type any 8 shit numbers on your keyboard!")
elif (z == 10 and "numb" in x.lower()):
    print (" who generates that long numbers u dumb! \n close your eyes and type any 10 shit numbers on your keyboard!")
elif (z == 12 and "numb" in x.lower()):
    print (" who generates that long numbers u dumb! \n close your eyes and type any 12 shit numbers on your keyboard!")
   