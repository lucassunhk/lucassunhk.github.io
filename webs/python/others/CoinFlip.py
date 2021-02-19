import random
def Coinflip():
    X = random.randint(1,2)
    y = input("Start? ")
    if y == "Yes":
        print("STARTING PROGRAM...")
        if X == 1:
            print("Heads!")
            print("---")
        else:
            print("Tails!")
            print("---")
        n = input("Try again (Yes/No)? ")
        if n == "Yes":
            print("RESTARTING PROGRAM...")
            Coinflip()
        elif n == "yes":
            print("RESTARTING PROGRAM...")
            Coinflip()
    elif y == "yes":
        print("STARTING PROGRAM...")
        if X == 1:
            print("Heads!")
            print("---")
        else:
            print("Tails!")
            print("---")
        n = input("Try again (Yes/No)? ")
        if n == "Yes":
            print("RESTARTING PROGRAM...")
            Coinflip()
        elif n == "yes":
            print("RESTARTING PROGRAM...")
            Coinflip()
        else:
            exit()
    else:
        exit()
Coinflip()
