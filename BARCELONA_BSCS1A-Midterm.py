# David Bryan Barcelona 
# BSCS 1A
#EPIC MIDTERM OUTPUT

from turtle import *
import turtle

turtle.title("Mandala Art - BARCELONA")
turtle.bgcolor("#222831")

def circle():
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(3)
    t.pencolor("#11999E")
    t.speed(0)
    t.goto(0,20)
    for i in range(20):
        t.circle(50)
        t.left (20)

def squares():
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(3)
    t.pencolor("#CCA8E9")
    t.speed(0)
    t.penup()
    t.goto(0,20)
    t.pendown()
    for i in range(8):
        for i in range(4):
            t.forward(110)
            t.left(90)
        t.left(45)
        for i in range(4):
            t.forward(110)
            t.left(90)
        for i in range(4):
            t.forward(140)
            t.left(90)
        t.left(45)
        for i in range(4):
            t.forward(200)
            t.left(90)

def circlepatt():
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(3)
    t.speed(0)
    t.pencolor("#EAFFD0")
    for i in range (40):
        t.penup()
        t.goto(0,20)
        t.pendown()
        t.circle(10)
        t.right(9)
        t.forward(200)
        t.pendown()
        t.circle(30)
        
def spirocircle():
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(3)
    t.speed(0)
    t.pencolor("#30E3CA")
    for i in range (40):
        t.goto(0,20)
        t.right(9)
        t.pendown()
        t.circle(130)        

def squarepatt():
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(3)
    t.speed(0)
    t.pencolor("#EEEEEE")
    for i in range(200):
        t.goto(0,20)
        t.right(9)
        t.forward(360)
        t.penup()
        t.right(220)
        for x in range(4):
            t.pendown()
            t.forward(40)
            t.right(90)
            t.forward(40)
            
def squarepatt2():
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(4)
    t.speed(0)
    t.pencolor("#71C9CE")
    for i in range(40):
        t.goto(0,20)
        t.right(9)
        t.forward(548)
        t.penup()
        t.right(90)
        for x in range(4):
            t.pendown()
            t.forward(50)
            t.right(90)
            t.forward(50)   
             
def circlepatt2():
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(4)
    t.speed(0)
    t.pencolor("#FFC7C7")
    for i in range (100):
        t.penup()
        t.goto(0,20)
        t.circle(20)
        t.right(5)
        t.forward(610)
        t.pendown()
        t.circle(60)
        
circle()
squares()        
circlepatt()
spirocircle()
squarepatt()
squarepatt2()
circlepatt2()

turtle.exitonclick()

