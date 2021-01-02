import a_python_quest01


#import madlibs

#import number_guess


class Horus:
  """#This is how we do it"""
  def __init__(self, name, time):
    """#This constuctor is used to reduce the time it takes to create new variables after giving it this class"""
    self.name = name
    self.time = time
    print("I am {} and my phone is set to {}".format(self.name,self.time))

john = Horus("John", "10am")
help(Horus)