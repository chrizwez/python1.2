def test(drones, waters):
  times = int(drones) * int(waters)
  print(times)


test(1,2)


def reg(hour, light, carries):
  time = hour + light/60 + carries/3600
  return time

huis = reg(2,2,2)

print(huis)


def test(drones, waters):
  times = int(drones) * int(waters)
  return times

input1 = input("How many drones do you see? ")
input2 = input("How many litres of water is there? ")

output1 = test(input1, input2)
print(output1)