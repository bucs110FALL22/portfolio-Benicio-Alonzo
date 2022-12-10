# author: Benicio Alonzo
# CS 110 - dog(project name)
# abstract: Proxy class to get random images from API

import requests
import pygame
import io
try:
  from urllib2 import urlopen
except ImportError:
  from urllib.request import urlopen


class Dog_image:

    def __init__(self):
        self.url = 'https://dog.ceo/api/breeds/image/random'
        self.DISPLAY_WIDTH = 300
        self.DISPLAY_HEIGHT = 300
        self.white = (255,255,255)
        self.img_size = (300,200)
        self.WAIT_TIME = 10000
      
    def get_pic(self):
        print("Calling API")
        pygame.init()
        r = requests.get(self.url)
        dog = r.json()
        image_url = (dog['message'])
        image_str = urlopen(image_url).read()
        image_file = io.BytesIO(image_str)
    
        display = pygame.display.set_mode([self.DISPLAY_WIDTH,self.DISPLAY_HEIGHT])
        display.fill(self.white)
        image = pygame.transform.scale(pygame.image.load(image_file),(self.img_size))
        display.blit(image,(0,0))
        pygame.display.flip()
        pygame.time.wait(self.WAIT_TIME)

    def change_category(self, category):
        pass
        #self.url = #...
        