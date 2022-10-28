import turtle
import random

window = turtle.Screen()

def draw_face ( pen):
 
  pen.color("black")
  pen.shape("classic")
  SIDE_LENGTH = 100
  NUM_SIDES = 4
  angle = 360/NUM_SIDES
  for i in range(NUM_SIDES):
    pen.forward(SIDE_LENGTH)
    pen.right(angle)


def draw_ear (pen ):
  
  pen.color("black")
  pen.shape("classic")
  SIDE_LENGTH = 30
  NUM_SIDES = 3
  angle = 360/NUM_SIDES
  pen.fillcolor("black")
  pen.begin_fill()
  for i in range(NUM_SIDES):
    pen.forward(SIDE_LENGTH)
    pen.left(angle)
  pen.end_fill()


def draw_eye(coords,pen):
  pen.color("black")
  pen.shape("classic")
  ANGLE1 = 60
  ANGLE2 = 120
  SIDE_LENGTH = 15
  pen.up()
  pen.goto(coords)
  pen.down()
  pen.left(ANGLE1)
  pen.forward(SIDE_LENGTH)
  pen.right(ANGLE2)
  pen.forward(SIDE_LENGTH)

def draw_mouth(pen):
  MOUTH_DISTANCE = 60
  ANGLE_TURN_LEFT60 = 60
  ANGLE_TURN_LEFT180 = 180
  FANG_DISTANCE = 50
  pen.color("black")
  pen.shape("classic")
  SIDE_LENGTH = 10
  NUM_SIDES = 3
  angle = 360/NUM_SIDES
  pen.fillcolor("red")
  coords = (-55,-20)
  pen.up()
  pen.goto(coords)
  pen.down()
  pen.left(ANGLE_TURN_LEFT60)
  pen.fd(MOUTH_DISTANCE)
  pen.left(ANGLE_TURN_LEFT180)
  pen.begin_fill()
  for i in range(NUM_SIDES):
    pen.forward(SIDE_LENGTH)
    pen.left(angle)
  pen.end_fill()
  pen.fd(FANG_DISTANCE)
  pen.begin_fill()
  for i in range(NUM_SIDES):
    pen.forward(SIDE_LENGTH)
    pen.left(angle)
  pen.end_fill()

def draw_whiskers_left(pen):
  DISTANCE_20 = 20
  ANGLE_60 = 60
  DISTANCE_15 = 15
  DISTANCE_10 = 10
  ANGLE_120 = 120
  pen.color("black")
  pen.shape("classic")
  num_whiskers = 4
  pen.up()
  pen.fd(DISTANCE_20)
  pen.down()
  pen.left(ANGLE_60)
  for i in range(num_whiskers):
    pen.fd(DISTANCE_15)
    pen.rt(ANGLE_60)
    pen.up()
    pen.fd(DISTANCE_10)
    pen.down()
    pen.rt(ANGLE_120)
    pen.fd(DISTANCE_15)


def draw_whiskers_right(pen):
  ANGLE_60 = 60
  ANGLE_240 = 240
  ANGLE_120 = 120
  DISTANCE_80 = 80
  DISTANCE_15 = 15
  DISTANCE_10 = 10
  pen.color("black")
  pen.shape("classic")
  pen.rt(ANGLE_240)
  pen.up()
  pen.fd(DISTANCE_80)
  pen.down()
  pen.rt(ANGLE_60)
  num_whiskers = 2
  for i in range(num_whiskers):
    pen.fd(DISTANCE_15)
    pen.left(ANGLE_60)
    pen.up()
    pen.fd(DISTANCE_10)
    pen.down()
    pen.left(ANGLE_120)
    pen.fd(DISTANCE_15)  
def random_drops():
  num_drops = random.randrange(10,30)
  return num_drops
def blood_drops(num_drops):
  blood = turtle.Turtle()
  blood.color("red")
  blood.shape("classic")
  blood.fillcolor("red")
  for i in range(num_drops):
    SIDE_LENGTH_STAR = 10
    ANGLE_STAR = 144
    NUM_LINES_STAR = 5
    drop_x = random.randrange(-120,100)
    drop_y = random.randrange(80,100)
    blood_drop = drop_x,drop_y
    blood.up()
    blood.goto(blood_drop)
    blood.down()
    blood.begin_fill()
    for i in range(NUM_LINES_STAR):
      blood.forward(SIDE_LENGTH_STAR)
      blood.rt(ANGLE_STAR)
    
    blood.end_fill()
    
  
def start(pen):
  COORDS_START = (-75,50)
  pen.up()
  pen.goto(COORDS_START)
  pen.down()
def main():
  pen = turtle.Turtle()
  COORDS_EYE1 = (-60,15)
  COORDS_EYE2 = (-10,15)
  FORWARD_70 = 70
  ANGLE_60 = 60
  start(pen)
  draw_face(pen)
  draw_ear(pen)
  pen.fd(FORWARD_70)
  draw_ear(pen)
  draw_eye(COORDS_EYE1,pen)
  pen.left(ANGLE_60)
  draw_eye(COORDS_EYE2,pen)
  draw_mouth(pen)
  draw_whiskers_left(pen)
  draw_whiskers_right(pen)
  random_drops()
  num_blood = random_drops()
  blood_drops(num_blood)
  

main()

window.exitonclick()
