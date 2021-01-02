# project to choose correct word

#0. import & variables
import time
load = []


#1. Load question and answer
def loading():
  x = open("madlibs.txt","r")
  y = x.read()
  z = y.split(".")
  a = len(z)
  i = 0
  for i in range(a):
    b = z[i]
    c = b.split(";")
    load.append(c)
    i += 1
    print(load)
  return load



#2. print out question and test against answer
def queries(loads):
  a = len(loads)
  x = 0
  for i in range(a):
    b = loads[x][0]
    c = loads[x][1]
    f = c.strip(" ")
    e = 0
    print("round")
    while e < 1:
      d = input(b)
      if d == f:
        print("You are correct!")
        time.sleep(2)
        e += 1
      else:
        print("Try again")
    x += 1
    
    




#CallOuts
loads = loading()
queries(loads)