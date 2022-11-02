import time

class Animal:
  def __init__(self,name,animal_species):
    self.type = animal_species
    self.adopted = None
    self.name = name
    self.id = time.strftime("%d%m%M%S")
    self.arrived = time.strftime("%d/%m/%Y")
    
     
  def set_adopted(self):
    self.adopted = time.strftime("%d/%m/%Y")
    
  def __str__(self):
      result_str = f"{self.name}[{self.type}]"
      result_str += f"\narrived: {self.arrived}"
      result_str += f"\nadopted:{self.adopted}"
      return result_str
      
    
def main():
  winston = Animal("Winston","monkey")
  winston.set_adopted()
  print(winston)

main()