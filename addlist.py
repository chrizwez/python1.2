food = ['carrot','apple']

def addfood(newfood):
  food.append(newfood)
  print (food)

for i in range(2):
  addfood(input("What do you own? "))