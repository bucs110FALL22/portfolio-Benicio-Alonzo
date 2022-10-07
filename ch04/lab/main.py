import pygame
import random
import math
pygame.init()

radius_dot = (5)
dot_color_in1 = "red"
dot_color_miss1 = "green"
dot_color_in2 = "orange"
dot_color_miss2 = "purple"
color_circle = "blue"
center = [100,100]
screen_size = [200,200]
radius_Board = (100)
color_line = "black"
length_lineH = [(0,100),(200,100)]
length_lineV = [(100,0),(100,200)]
closed = True
dart1 = []
dart2 = []
width = (200)
is_in_circle = []
x1 = (100)
y1=(100)
score1 = (0)
score2 = (0)
hit_box_width = (100)
hit_box_height = (50)
color_box_red = "red"
color_box_orange = "orange"
prediction = "hold"
orange_rect = (0,0,100,200)
red_rect = (100,0,200,200)
player_side = True

window = pygame.display.set_mode(screen_size)

while player_side == True:
  mouse_x, mouse_y = pygame.mouse.get_pos()
  orange_button =         pygame.draw.rect(window,color_box_orange,orange_rect)
  red_button =    pygame.draw.rect(window,color_box_red,red_rect)             
  pygame.display.flip()
  pygame.time.wait(700)
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        if orange_button.collidepoint(mouse_x,mouse_y):
            prediction = "orange"
            player_side = False
        else:
          prediction = "red"
          player_side = False






window.fill("white")
pygame.draw.circle(window,color_circle,center,radius_Board)
pygame.draw.lines(window,color_line,closed,length_lineH)
pygame.draw.lines(window,color_line,closed,length_lineV)



for i in range(10):
  
  dart_x1 = random.randrange(0,200)
  dart_y1 = random.randrange(0,200)
  dart1 = dart_x1, dart_y1
  distance_from_center1 = math.hypot(x1-dart_x1, y1-dart_y1)
  is_in_circle1 = distance_from_center1 <= width/2
  
  dart_x2 = random.randrange(0,200)
  dart_y2 = random.randrange(0,200)
  dart2 = dart_x2, dart_y2
  distance_from_center2 = math.hypot(x1-dart_x2, y1-dart_y2)
  is_in_circle2 = distance_from_center2 <= width/2
  
  
  if is_in_circle1 == False :
    dot_color1 = dot_color_miss1
  else :

    dot_color1 = dot_color_in1

  if is_in_circle2 == False :
    dot_color2 = dot_color_miss2
  else :

    dot_color2 = dot_color_in2
    
  pygame.draw.circle(window,dot_color1,dart1,radius_dot)
  pygame.time.wait(700)
  pygame.display.flip()
  pygame.time.wait(700)
  pygame.draw.circle(window,dot_color2,dart2,radius_dot)
  pygame.display.flip()
  pygame.time.wait(1000)

  
  if is_in_circle1 == True:
    score1 = score1 + 1
    print("Player 1 throws...hit")
  else:
    print("Player 1 throws...miss")
  if is_in_circle2 == True:
    score2 = score2 + 1
    print("Player 2 throws...hit")
  else :
    print("Player 2 throws... miss")

if score1 > score2 :
  print("The winner is player 1, they scored ", score1 , "points")
 
elif score2 > score1:
  print("The winner is player 2, they scored", score2, "points")
elif score1 == score2:
  print("The game ended in a tie")

if prediction == "red" and score1>score2 :
  print("You were correct the ", prediction, "player won")
elif prediction == "orange" and score2>score1 :
  print("You were correct the ", prediction, "player won")
elif prediction == "red" and score1<score2:
  print("You were incorrect guess better next time")
elif prediction == "orange" and score2<score1:
  print("You were incorrect guess better next time")
else :
  print("No one won the game so you were still wrong")
pygame.time.wait(3000)

  


