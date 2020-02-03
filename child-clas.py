class Parent:        # define parent class
   def PMethod(self):
      print ('Calling parent method')

class Child(Parent): # define child class
   def CMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.CMethod()    
c.PMethod()