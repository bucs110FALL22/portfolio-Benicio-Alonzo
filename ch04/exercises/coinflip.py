import turtle
import random

turtwig = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("white")
turtwig.shape("turtle")
turtwig.speed(0)

distance = 10
angle = 90
is_in_screen = True
colors = ["purple","orange","green"]


while is_in_screen:
  coin = random.randrange(0,2)
  if coin == 0 :
    turtwig.left(angle)
  else:
    turtwig.right(angle)
    turtwig.forward(distance)


    turtle_x = turtwig.xcor()
    turtle_y = turtwig.ycor()

    x_range = window.window_width()/2
    y_range = window.window_height()/2

    turtwig.color(colors[0])
    colors.append(colors.pop(0))

    if abs(turtle_x) > x_range or abs(turtle_y) > y_range :
      is_in_screen = False

window.bgcolor("red")
window.exitonclick()


