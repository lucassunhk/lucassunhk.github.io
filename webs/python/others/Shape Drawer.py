n = input("Color of shape (goldenrod, gold, red, yellow, green, blue, black): ")
x = input("Shape (Triangle, Square, Pentagon, Hexagon, Circle): ")
z = int(input("Length of each side / diameter: "))
import turtle
t = turtle.Pen()
t.begin_fill()
t.hideturtle()
t.color(n)
if x == "Triangle":
    for i in range(0,3):
        t.forward(z)
        t.left(120)
elif x == "Square":
    for i in range(0,4):
        t.forward(z)
        t.left(90)
elif x == "Pentagon":
    for i in range(0,5):
        t.forward(z)
        t.left(72)
elif x == "Hexagon":
    for i in range(0,6):
        t.forward(z)
        t.left(60)
elif x == "Circle":
    t.circle(z)
else:
    print("Please run the program again. Try typing the shape / color exactly as displayed.")
    exit()
t.end_fill()
