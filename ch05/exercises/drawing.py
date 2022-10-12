import turtle

window = turtle.Screen()


num_sides = int(input("How many sides for your wonderful shape: "))
side_length = int(input("How long do you wish each side to be: "))

def draweqshape (num_sides,side_length):
  
  Turtwig = turtle.Turtle()
  Turtwig.color("blue")
  Turtwig.shape("turtle")
  angle = 360/num_sides
  for i in range(num_sides):
    Turtwig.forward(side_length)
    Turtwig.right(angle)
    


draweqshape(num_sides,side_length)
window.exitonclick()