import random                                 #imports module
x = open('C:\\Users\\xxx\\Magic8Ball.txt')  #opens file
response = x.readlines()
Boolean = True                                #uses variable to start infinite loop
while (Boolean):
    n = input("Question or Quit: ")           #asks for input
    if n == "Quit":                           #exits program when quit is entered
        break
    elif n == "quit":
        break
    else:
        v = len(response) - 1                 #randomly selects a reply from the opened file and prints it
        y = random.randint(0,v)
        print(response[y])
