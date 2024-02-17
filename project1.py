import random
Cnumber=random.randrange(1,101)
userInput=int(input("Enter Your Number:---"))
if userInput>Cnumber:
    print("Computer Number,Cnumber")
    print("Your guess number is too high")
elif Cnumber>userInput:
    print("Your guess nomber is too low")
else:
    print("Your guess number is equal")
    