import random
def Diceroll():
    X = random.randint(1,6)
    y = input("Start? ")
    if y == "Yes":
        print("STARTING PROGRAM...")
        print("Dice roll is %s." %X)
        print("---")
        n = input("Try again (Yes/No)? ")
        if n == "Yes":
            print("RESTARTING PROGRAM...")
            Diceroll()
        elif n == "yes":
            print("RESTARTING PROGRAM...")
            Diceroll()
    elif y == "yes":
        print("STARTING PROGRAM...")
        print("Dice roll is %s." %X)
        print("---")
        n = input("Try again (Yes/No)? ")
        if n == "Yes":
            print("RESTARTING PROGRAM...")
            Diceroll()
        elif n == "yes":
            print("RESTARTING PROGRAM...")
            Diceroll()
        else:
            exit()
    else:
        exit()
Diceroll()
