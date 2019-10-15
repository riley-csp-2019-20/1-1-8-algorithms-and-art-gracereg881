import turtle as trtl
import random
turtle = trtl.Turtle()

# setting the size of the robot
turtle.pensize(2)

# setting the location of the robot
turtle.up()
turtle.goto(-250,-100)
turtle.down()

# set the color of the base of the house
turtle.fillcolor("navajowhite")
turtle.begin_fill()

# making the robot move forward
turtle.forward(500)

# create the side of the house
turtle.left(90)
turtle.forward(220)

# create the top of the house
turtle.left(90)
turtle.forward(500)

# create the other side of the house
turtle.left(90)
turtle.forward(220)
turtle.end_fill()

# change the location of the turtle to start the roof
turtle.up()
turtle.goto(-280,120)
turtle.down()

# create roof of house
turtle.fillcolor("saddlebrown")
turtle.begin_fill()
turtle.left(150)
turtle.forward(256)
turtle.right(60)
turtle.forward(308)
turtle.right(60)
turtle.forward(258)
turtle.right(120)
turtle.forward(565)
turtle.end_fill()

# make the window on the roof
turtle.up()
turtle.goto(-10,230)
turtle.down()
turtle.fillcolor("light blue")
turtle.begin_fill()
turtle.forward(50)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(80)
turtle.end_fill()
turtle.up()
turtle.goto(-10,185)
turtle.down()
turtle.left(90)
turtle.forward(50)
turtle.left(180)
turtle.forward(100)


# making the door
turtle.up()
turtle.goto(-85,-10)
turtle.down()
turtle.fillcolor("sienna")
turtle.begin_fill()
turtle.left(90)
turtle.forward(89)
turtle.right(90)
turtle.forward(65)
turtle.right(90)
turtle.forward(89)
turtle.right(90)
turtle.forward(65)
turtle.end_fill()

#create list
colorList=["cornsilk", "wheat","gold","khaki", "ivory","tan","burlywood","lemonchiffon","orange","bisque"]
randNum=random.randint(0,10)

color=colorList[randNum]

# making the doorknob
v=5
while v>0:
    randNum=random.randint(0,10)
    color=colorList[randNum]
    turtle.penup()
    turtle.goto(-100,-70)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    v+=1


wn = trtl.Screen()
wn.mainloop()