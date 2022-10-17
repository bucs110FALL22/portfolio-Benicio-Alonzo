def percentage_to_letter(score=0):
  print("What was the score of your last exam? : ")
  score = float(input(""))
  if score >= 90 and score < 100 :
    return("A")
  elif score >= 80 and score <90:
    return("B")
  elif score >= 70 and score < 80:
    return("C")
  elif score >= 60 and score < 70:
    return("D")
  elif score < 60:
    return("F")
  else:
    return("invalid input")
   
  return score


  

def is_passing(letter = None):
  
  if letter == "A" or letter ==  "B" or letter == "C" :
    return("You have passed")
  else:
    return("You have failed")

  



score_letter = percentage_to_letter()
passing = is_passing(score_letter)

print("The letter you deserved for this is  :  " + score_letter)
print(passing)
