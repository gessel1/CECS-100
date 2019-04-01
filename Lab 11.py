#Gideon Essel

import turtle
turtle.showturtle()

turtle.speed(10)
turtle.penup()
turtle.goto(0,350)
turtle.pendown()

#Ceiling
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(360)
turtle.forward(30)
turtle.setheading(45)
turtle.forward(300)
turtle.setheading(325)
turtle.forward(350)
turtle.setheading(360)
turtle.forward(30)
turtle.setheading(145)
turtle.forward(400)
turtle.setheading(180)
turtle.forward(50)

#Walls
turtle.goto(-172,150)
turtle.setheading(270)
turtle.pendown()
turtle.forward(450)
turtle.setheading(360)
turtle.forward(400)
turtle.setheading(90)
turtle.forward(520)
turtle.penup()

#Doors
turtle.goto(-50,0)
turtle.pendown()
turtle.pencolor('brown')
turtle.setheading(270)
turtle.forward(300)
turtle.goto(-50,0)
turtle.setheading(360)
turtle.forward(100)
turtle.setheading(270)
turtle.forward(300)
turtle.penup()

#Windows.
#Windows 1
turtle.goto(-90,100)
turtle.pendown()
turtle.forward(30)
turtle.forward(30)
turtle.setheading(360)
turtle.forward(70)
turtle.setheading(90)
turtle.forward(60)
turtle.setheading(180)
turtle.forward(70)
turtle.penup()

#Windows 
turtle.goto(90,100)
turtle.pendown()
turtle.setheading(270)
turtle.forward(30)
turtle.forward(30)
turtle.setheading(360)
turtle.forward(70)
turtle.setheading(90)
turtle.forward(60)
turtle.setheading(180)
turtle.forward(70)

#Chimney

turtle.penup()
turtle.goto(200,230)
turtle.pendown()
turtle.setheading(90)
turtle.forward(70)
turtle.setheading(180)
turtle.forward(55)
turtle.setheading(270)
turtle.forward(20)
