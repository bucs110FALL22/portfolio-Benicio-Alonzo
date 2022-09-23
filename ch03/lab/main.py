import turtle #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# 5. Your PART A code goes here

num_m = random.randrange(1,101)
michelangelo.forward(num_m)
num_l = random.randrange(1,101)
leonardo.forward(num_l)
window.delay(700)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(10):
  num_LeoLoop = random.randrange(1,11)
  num_MikeLoop = random.randrange(1,11)
  michelangelo.forward(num_MikeLoop)
  leonardo.forward(num_LeoLoop)

window.delay(700)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
  # PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()

coords = []
num_sides = (4)
side_length =(35) 
offset = (50)
color = "aquamarine"

for i in range(num_sides):
  theta = (2.0 * math.pi * i) /   num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.draw.polygon(window,color,coords)
pygame.display.flip()
pygame.time.wait(700)
window.fill("black")

coords = []
num_sides = (6)
for i in range(num_sides):
  theta = (2.0 * math.pi * i) /   num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.draw.polygon(window,color,coords)
pygame.display.flip()
pygame.time.wait(700)
window.fill("black")

coords = []
num_sides = (9)
for i in range(num_sides):
  theta = (2.0 * math.pi * i) /   num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.draw.polygon(window,color,coords)
pygame.display.flip()
pygame.time.wait(700)
window.fill("black")

coords = []
num_sides = (360)
for i in range(num_sides):
  theta = (2.0 * math.pi * i) /   num_sides
  x = side_length * math.cos(theta) + offset
  y = side_length * math.sin(theta) + offset
  coords.append((x,y))

pygame.draw.polygon(window,color,coords)
pygame.display.flip()
pygame.time.wait(700)
window.fill("black")



#window.exitonclick()
