#0. Import the correct items
import time
from random import random
from datetime import date
# 1. To ask a question if you wish to add any new questions/answers, if yes then ask Q then ask A. If no, then continue with the test

yes = ["y","Y","yes","Yes","YES","YEs"]
none = ["n","N","no","No","NO"]
# 1.1. To ask the question and limit to bootlean response YES or NO

#adding new q & a
     
  
  

#generate a random number

#to extract question bank



#do you have any new questions?


def quiz_begin(quizBank):
  x = quizBank
  i = 0
  #while i < len(x):
   # q = input(x[i][0])
    #print("The correct answer is:\n" x[i][1])
   # i += 1

def new_question(newquestions):  #Step 1
  temp = input("Do you want to add new queries/responses? (Y/N): ")
  if temp == ("Y") or temp == ("y"):
    add_question(temp)
  elif temp == ("N") or temp == ("n"):
    print("Thank you!")
    #quiz(temp)
  else:
    print("\nYou did not enter Y or N, please try again in...\n")
    new_question(1)

def add_question(addquestion):    #Step 1b
  question = input("\nWhat is the new question? \n")
  answer = input("\nWhat is the correct response? \n")
  update = (question + "; " + answer + "\n")
  #print("\nQuestion bank has been updated with:\n" + update)
  text = open("pythonquest.txt","a")
  text.write(update)
  text.close()
  #text = open("pythonquest_num.txt","a")
  #text.read()
  new_question(update)

def quiz_prep_extract():     #Step 2
  text = open("pythonquest.txt","r")
  text1 = text.read()
  text.close()
  text2 = text1.split("\n")
  countz = len(text2)
  #print(countz)
  count = str(countz)
  #print("john")
  #print = (len(text2))
  #count = len(text2)
  return text2, count

def quiz_prep_load(text, count):  #Step 3 (Place extract into dict)
  #print(text,count) 
  quiz_bank = {}
  count1 = int(count) - 1
  for i in range(count1):
    y = text[i]
    #print(y)
    #q = input("Does this look ok, before split?")
    y = y.split(";")
    #print(y)
    #q = input("Does this look ok, after split?")
    x = str(i)
    quiz_bank[x] = y
  #print(quiz_bank)
  #q = input("Does this look right?")
  #print("Whoooo")
  return quiz_bank   #this seems to be in the right format
  
def quiz_continue():   #Step 4 #continue with quiz
  x = input("Do you wish to continue to the quiz? ")
  maximum = 0
  i = 0
  j = int(var01[1])-1
  #print(j)
  if x == "yes" or x == "Yes" or x == "Y" or x == "y":
    while i < 1:
      maximum = input("How many questions this time? ")
      maxi = int(maximum)
      if maxi > j:
        print("You have to choose a number below", (var01[1]))
      else:
        i += 1
    return maximum
    #please = input("What?")
  elif x == "no" or x == "No" or x == "N" or x == "n":
    print("See you next time? ")
    exit()
 
def quiz_prep_random(quantity, maxim):   #Step 5
  random_num = []
  maxiz = int(maxim) - 2
  i = 0
  while i < int(quantity):
    y = round(random()*100)
    if not y in random_num:
      if y < int(maxiz):
        random_num.append(y)
        i += 1
  #print(random_num)
  #print(maxiz)
  #a = input("random ok")
  return random_num

def quiz_generate(random, quiz_banks):   #Step 6
  x = {}
  rand = len(random) #number of random numbers
  #print(rand)
  #a = input("Rand ok?")
  #print(random)   #the random numbers
  #a = input(" ok?")
  #print(quiz_banks)
  #a = input("quizbanks ok?")
  i = 0
  #y = random[i]
  #print(quiz_bank[str(y)])
  #a = input("quizbank 0 ok?")
  while i < rand:
    y = random[i]
    #print(y)
    #print(quiz_bank[str(y)])
    #a = input("quizzy Ok???")
    x[i] = quiz_bank[str(y)]
    i += 1
  #x["test1"] = quiz_banks[29]
  #x["test2"] = quiz_banks[30]
  #x["test3"] = quiz_banks[32]
  #quiz = len(quiz_banks)
  #print(len(quiz_banks))
  #print(x)
  return x
  #print("Completed")
  #print(len(quiz)

def quiz_start(permission):
  response = 0
  total = len(permission)
  today = date.today()
  #print(today)
  i = 0
  while i < len(permission):
    print("\nThe next questions is:")
    q = input(permission[i][0] + "\n")
    #print("\nYour response was:\n " + q)
    print("\nThe answer is:\n" + permission[i][1])
    a = input("\nIs your answer correct? ")
    if a == "y" or a == "Y" or a == "Yes" or a == "yes":
      response += 1
    i += 1
  score = int(response/total*100)
  results = (str(today) + ": Your score is " + str(score) + "% out of " + str(total) + " questions\n")
  print(results)
  x = open("pythonquest_score.txt","a")
  x.write(results)
  x.close()
  return results

new_question(1)   #Step 1
var01 = (quiz_prep_extract()) #Step 2
#print(var01) #txt file
#a = input("Var01 Stop?")
quiz_bank = quiz_prep_load(var01[0], var01[1]) #Step 3
#print(quiz_bank) #dict-quiz
#a = input("Quizbank Stop?")
#
quizzes = var01[0] #extract quizzes
#print(quiz_bank)  #Full quiz Bank
#dee = input("quizes printed?") #pause
#
maxim = quiz_continue() #Step 4
#print(maxim) #number of questions
#a = input("Maxim Stop?")
random = quiz_prep_random(maxim, var01[1]) #Step 5
#print(random) #random numbers
#a = input("Random Stop?")
#
#print(maxim)
#print(var01[0])
#print(var01[1])
#ready = input("are you ready?")
#print(random)
#print(var01[0])
#
permission = quiz_generate(random, quiz_bank) #Step 6
#print(permission)
#a = input("Permission Stop?")

# 3. To setup a randomized number generator, with max as count of dict entries
quiz_start(permission) #Step 7

# 4. 