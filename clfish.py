class Fish :
    data = {} 
    def __init__(self,speed) :
        self.speed = speed 
        print("New fish is born")
    
    def breath(self):
        print("Breathing oxygen under water")
    
    def swim(self):
        print("swimming with a speed of %d "%self.speed)
    
    def __getattr__(self,attr) :
        if(attr in Fish.data) :
            return Fish.data[attr]
    
    def __setattr__(self,attr,val) :
        Fish.data[attr] = val 

class Shark(Fish) :
    def __init__(self):
        super().__init__(100)
    
    def kill(self):
        print("I kill others for food ")

koi = Fish(60)
koi.breath()
koi.swim()
koi.skeleton = "cartileges"

bs = Shark()
bs.breath()
bs.swim()
bs.kill()
print(bs.skeleton)

'''The getattr(obj, name[, default]) − to access the attribute of object.

The hasattr(obj,name) − to check if an attribute exists or not.

The setattr(obj,name,value) − to set an attribute. 
If attribute does not exist, then it would be created.

The delattr(obj, name) − to delete an attribute.'''