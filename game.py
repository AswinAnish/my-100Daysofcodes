import turtle
import time 
import random

delay = 0.1

score =0
high_score = 0

wn= turtle.Screen()
wn.title("Snake Mania")
wn.bgcolor('white')
wn.setup(width=600,height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)

head.direction = "stop"


food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


segments = []
#turtle.forward(50)
#turtle.right(60)


sc=turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("score:0 High Score:0",align = "center",font=("ds-digital",24,"normal"))


wn.mainloop()