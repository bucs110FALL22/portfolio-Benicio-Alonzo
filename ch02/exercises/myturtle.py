import turtle
window = turtle.Screen()

my_turtle = turtle.Turtle()
length=50
num_sides=int(input("Enter the number of sides "))
angle = 360/num_sides

my_turtle = turtle.color("purple")
my_turtle = turtle.shape("turtle")


for i in [angle]*num_sides:
  my_turtle=turtle.forward(length)
  my_turtle=turtle.rt(i)


# first square in purple

my_turtle = turtle.up()
my_turtle = turtle.color("red")
my_turtle = turtle.fd(70)
my_turtle = turtle.down()

for i in [angle]*num_sides:
  my_turtle=turtle.forward(length)
  my_turtle=turtle.rt(i)


window.exitonclick()