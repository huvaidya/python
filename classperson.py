class Person:
    country = "India" #class variable
    counter = 0       
    def __init__(self,name):
        self.name = name 
        self.hands = 2
        self.legs = 2
        self.lp = 30
        Person.counter += 1
    
    def smoke(self):
        print(self.name + " is smoking...")
        self.lp -= 1
        self.testlp()
    
    def yoga(self) :
        print(self.name + " is doing yoga")
        self.lp += 2
        self.testlp()
    
    def testlp(self):
        print("Lungpower is ",self.lp)

    def run(self): 
        print(self.name , " running ...")

    def __del__(self):
        Person.counter -= 1
        print(self.name + " dying...")

print("****Program begins*****")
print("===== Population is " , Person.counter, " ======")

hari = Person("Hariprasad")
print("The name is " , hari.name )
print("===== Population is " , Person.counter, " ======")

alex = Person("Alexander")
print("The name of alex is " , alex.name)
print("===== Population is " , Person.counter, " ======")

hari.run() #hariprasad running...
alex.run()

print("Hari has {} hands and {} legs".format(hari.hands , hari.legs))

hari.yoga()

alex.smoke()
alex.smoke()

#alex.__lp = 99 
alex.smoke()
#print(alex.__dir__())
alex.yoga()

#del alex

print("{} stays in {}".format(hari.name,hari.country))
Person.country = "Vietnam"
print("{} stays in {}".format(alex.name,alex.country))
print("****** Program over *****")