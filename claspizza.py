class Pizza :
    def __init__(self):
        self.base()
        self.toppings()
        self.bake()
    
    def base(self):
        print("Base is made of wheat")
    
    def toppings(self) :
        print("Adding onions mushrooms and tomatoes")
    
    def bake(self) :
        print("Baking at 200 deg ")

class CheesePizza(Pizza):
    def toppings(self):
        print("Add cheesy pieces") 
        super().toppings()

o1 = Pizza()
print("-------Second time-------")
o2 = CheesePizza()