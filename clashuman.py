class Human:
    def __init__(self):
        self.hands = 2 
        self.legs = 2
        print("human is born")
    
    def walk(self) :
        print("Walking like a human")

    def sound(self):
        print("Human sound")

class Swimmer :
    def __init__(self) :
        print("swimmer is born")
    
    def swim(self) :
        print("Swimming")

    def sound(self):
        print("swimming sound")
    
class Student (Swimmer,Human):
    def study(self):
        print("Reading books...")

hari = Student()
hari.walk()
hari.swim()
hari.study()
hari.sound()