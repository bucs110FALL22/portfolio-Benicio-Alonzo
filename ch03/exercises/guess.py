import random 

num = random.randrange(1,11)
num_guesses = 0
correct_guess = False



for i in range(3):
  if not correct_guess:
    guess_num = int(input("Please enter a guess from 1-10:"))
   #num_guesses += 1
  if guess_num > num:
      print("your guess is too high")
  elif guess_num < num:
    print("your guess is too low")
  else:
    print("YOU ARE CORRECT")
    break
  





#If the user guesses on the first try you can use a break to stop the loop
