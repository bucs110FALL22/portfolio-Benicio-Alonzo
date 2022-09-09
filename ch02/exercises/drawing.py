import turtle
window = turtle.Screen()

my_turtle = turtle.Turtle()
num_length= int(input("enter the length for the sides "))
num_sides=int(input("Enter the number of sides "))
angle = 360/num_sides

my_turtle = turtle.color("green")
my_turtle = turtle.shape("turtle")


for i in [angle]*num_sides:
  my_turtle=turtle.forward(num_length)
  my_turtle=turtle.rt(i)


window.exitonclick()