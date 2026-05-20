from functools import reduce

data = {}
print("The computer will take sub and marks for that sub as a input from you...Type \'stop\' when no more subjects are need to be entered. ")

while(True):                                                                                       #adding contents in dict-data
    user = input("Sub: ")
    if(user == "stop"):
        break
    value = int(input("marks: "))
    data.update({user : value})
fm = int(input(("You pressed stop. Whats the FM?: ")))
# print(" ".join(data.keys()))
def add(a, b):
    return a + b
print("The average is:", int((reduce(add, data.values())))/int(len(data.values())))                #average
print("Percentage is:", (int(reduce(add, data.values()))/fm)*100)                                  #percentage
highest_sub = max(data, key=data.get)
print("You got highest marks in the subject(s) in which you got:", data[highest_sub])
lowest_sub = min(data, key=data.get)
print("Improvement is required in the subject(s) you got:", data[lowest_sub])                      #highest and lowest marks
print("Credits:\nWas created by: \"Arnav Saket\"")
d = int((reduce(add, data.values())))/int(len(data.values()))
e = (int(reduce(add, data.values()))/fm)*100
o = open("stats.csv", "w")                                                                         #writing the contents in a csv file
o.write(a.items())               
o.write(f"Average-{d}               ")
o.write(f"Percentage-{e}")

o.close
