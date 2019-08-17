import turtle
import time

wn = turtle.Screen()
wn.bgcolor("black")

# title
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Traffic Light", align="center", font=("futura", 50, "bold"))

# box
box = turtle.Turtle()
box.color("yellow")
box.width(3)
box.hideturtle()
box.penup()
box.goto(-30,90)
box.pendown()
box.fd(60)
box.rt(45)
box.fd(40)
box.rt(45)
box.fd(170)
box.rt(45)
box.fd(40)
box.rt(45)
box.fd(60)
box.rt(45)
box.fd(40)
box.rt(45)
box.fd(170)
box.rt(45)
box.fd(40)


# Red light
redligh = turtle.Turtle()
redligh.shape("circle")
redligh.shapesize(3)
redligh.color("grey")
redligh.penup()
redligh.goto(0,50)

# Yellow light
yellowlight = turtle.Turtle()
yellowlight.shape("circle")
yellowlight.shapesize(3)
yellowlight.color("grey")
yellowlight.penup()
yellowlight.goto(0,-25)

# Green light
greenlight = turtle.Turtle()
greenlight.shape("circle")
greenlight.shapesize(3)
greenlight.color("grey")
greenlight.penup()
greenlight.goto(0,-100)

while True:
    yellowlight.color("grey")
    redligh.color("red")
    time.sleep(4)

    redligh.color("grey")
    greenlight.color("green")
    time.sleep(2)

    greenlight.color("grey")
    yellowlight.color("yellow")
    time.sleep(3)




wn.mainloop()