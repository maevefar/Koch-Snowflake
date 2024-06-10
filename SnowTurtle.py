#Author: Maeve Farley 

import turtle
from turtle import *
import tkinter as tk

tur = turtle.Turtle()
#initalizes global variable to None
window_width = None 
window_height = None 
order = None
size = None
color = None

def draw_koch_snowflake(order, size):
    if order == 1: #base case, draws line
        tur.forward(size)
        return
    else: #recursively calls the function to draw the point
        draw_koch_snowflake(order-1, size/3) #size/3 bc each new line is 1/3 the size 
        tur.right(60) #inner angle of triangle
        draw_koch_snowflake(order-1, size/3)
        tur.right(-120) #outer angle of triangle
        draw_koch_snowflake(order-1, size/3)
        tur.right(60) #inner angle triangle
        draw_koch_snowflake(order-1, size/3)

def draw_snowflake(order, size, color): 
    turtle.tracer(0) #disables tracer 
    tur.begin_fill()
    tur.fillcolor(color)
    tur.pencolor(color)
        
    for i in range(3):
        draw_koch_snowflake(order, size)
        tur.left(120) #outer angle of each angle in a triangle(180-60)
    tur.end_fill()

def resize_window(event):
    #redraws the snowflake based on the user adjusted window size 
    tur.clear()
    new_width = turtle.getcanvas().winfo_width()
    new_height = turtle.getcanvas().winfo_height()
    new_len = min(new_width, new_height) * 0.8
    turtle.penup()
    turtle.setpos(-new_len/2, -new_len/2)
    turtle.pendown()
    draw_snowflake(order, new_len/3, color)

def main():
    global window_width, window_height, order, size, color
    turtle.setup(800,800) #sets inital window dimensions
    turtle.onscreenclick(None)  # Disable turtle's onclick events
    turtle.Screen().tracer(0) #disables tracer
    
    #user input
    order = int(turtle.textinput("Draw a Koch Snowflake!", "Order"))
    size = int(turtle.textinput("Size", "Size of Snowflake"))
    color = str(turtle.textinput("Colors: red, green, blue, pink, purple ", "What color do you want it to be? "))
    
    
    draw_snowflake(order,size,color)
    turtle.getcanvas().winfo_toplevel().bind("<Configure>", resize_window)  # Bind resize_square to window resize event
    turtle.Screen().update()
    
    while True:
        again = str(turtle.textinput("Again", "Would you like to draw another snowflake? (yes/no)"))
        if again.lower() != "yes": 
            break
        turtle.clearscreen() #clears the screen
        
        #user input
        order = int(turtle.textinput("Draw a Koch Snowflake!", "Order"))
        size = int(turtle.textinput("Size", "Size of Snowflake"))
        color = str(turtle.textinput("Colors: red, green, blue, pink, purple ", "What color do you want it to be? "))
    
        draw_snowflake(order,size,color) #draws the snowflake again 
        turtle.getcanvas().winfo_toplevel().bind("<Configure>", resize_window)
        turtle.Screen().update()
    
    turtle.mainloop() #keeps the screen open 

main()