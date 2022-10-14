import pygame
pygame.init()
display_width = 300
display_height = 300
display = pygame.display.set_mode([display_width,display_height])

display.fill([0,255,0])
pygame.display.flip()
color = "black"
Scale = 11
max_so_far = 0
start_num = 1
iters = {}
n=101
upper_limit = 20
max_val = ()
count = 0
result = 0
font = pygame.font.Font(None, 20)
pos= (10,10)
iters_new={}
new_display= pygame.transform.flip(display, False, True)



def sequence (n=0):
  count = 0
  while n != 1 :
    if n % 2 == 0 :
      n = n/2
      count += 1
    else :
      n = (n*3)+1
      count += 1
  
  
  print(count)
  return count

sequence(n)

for i in range(2,upper_limit+1):
  count = sequence(i)
  iters.update({i*Scale:count*Scale})
  
 
  iters[i]=count
  iters_new[i*Scale] = display_height-count*Scale
  coords = list(iters_new.items())
  
  if count > max_so_far:
    max_so_far = count
    max_val = str(max_so_far)
    display.blit(new_display,(0,0))
    msg = font.render("Max value of iterations is " + max_val , True, color)
    display.blit(msg, pos)
    
  if len(coords) > 1:
    pygame.draw.lines(display, color, False, coords)
    pygame.time.wait(1000)
    pygame.display.flip()
    











  
