class Brick_block:
  def __init__(self):
    self.broken = False #the brick blocks start not broken
    self.hit  = "coin" # the brick can release one coin
    self.multiple_hit = "1-up" # after the brick is hit multiple times it can release a 1-up shroom

class Mario:
  def __init__(self):
    self.powers = False #mario starts with no power ups
    self.big = False #mario starts small aka normal size
    self.pipe = True # mario starts coming out of a pipe

class Goomba:
  def __init__(self):
    self.spawn = True # the goomba spawns in
    self.stomp = False # the goomba doesnt start as being destroyed
    self.health = 1 # the goomba only has 1 life