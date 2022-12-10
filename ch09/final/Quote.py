# author: Benicio Alonzo
# CS 110 - dog(project name)
# abstract: Proxy class to get random facts about dogs

import requests
import pygame
class Quote:
  def __init__(self):
    print("Calling API")
    self.url = requests.get("https://animechan.vercel.app/api/random")
    
  def get_quote(self):
    response = requests.get("https://animechan.vercel.app/api/random")
    fact = response.json()
    print(fact['quote'])
    

    

  
