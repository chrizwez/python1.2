# computer number to be correctly guessed
from random import random

#1. random number
randnum = round(random()*10)


#2. input guessed
def guess():
  i = 0
  while i < 1:
    x = input("Guess the number? ")
    x = int(x)
    if x != randnum:
      if x > randnum:
        y = x - randnum
      else:
        y = randnum - x
      print("Please try again, " + str(x) + " is " + str(y) + " from the correct number")
    else:
      print("Success")
      i += 1

#3. clue (distance from num) & reduce score



guess()

#4. 
a = 0
def guess2():
  y = int(yournum)
  i = 0 
  mini = [0]
  maxs = [1000]
  while i < 1:
    x = min(maxs) - max(mini)
    x = round(x/2)
    x = min(maxs) - x
    print(x)
    if x > y:
      maxs.append(x)
    elif x < y:
      mini.append(x)
    elif x == y:
      i += 1
  print("Success")
            
          
        
  
  
yournum = input("Pick a number ")
guess2()