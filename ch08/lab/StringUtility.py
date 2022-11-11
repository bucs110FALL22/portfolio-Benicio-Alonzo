class StringUtility:
  def __init__ (self,string):
    self.string = string
  
  def __str__(self):
    result_str = self.string
    return result_str

  def vowels(self):
    
    count = 0
    for char in self.string:
      if char in "aeiouAEIOU":
        count = count + 1
    if count >=5 :
      count = "many"
      return count
    elif count < 5:
      return str(count)
      
  def bothEnds(self):
    
    if len(self.string) <= 2:
      string1 = ""
      return string1
    else:
     
      string1 = self.string[0:2] + self.string[-2:]
      return string1
    
    
  def fixStart(self):
    if len(self.string) <= 1:
      return self.string
    letter1 = self.string[0]
    count = 0
    for chr in self.string:
      if chr in letter1:
        count += 1 
    if count <= 1 :
      return self.string
    else:
      for i in range(len(self.string)+1):
        string1 = self.string.replace(letter1,"*")
        string2 = letter1 + string1[1:len(string1)+1]
        return string2
        
    
  def asciiSum(self):
    total = 0
    for i in range(len(self.string)):
      total = total + ord(self.string[i])
    return total
    
  def cipher(self):
    result = ""
    shift =len(self.string)
    for i in range(len(self.string)):
      if self.string[i].islower():
        value = (((( (ord(self.string[i])) - 97)+shift) %26)+97)
        result += chr(value)
      elif self.string[i].isupper():
        value1 = (((( (ord(self.string[i])) - 65)+shift) %26)+65)
        result += chr(value1)
      else:
        result += self.string[i]
    return result
      
      
      
      


    