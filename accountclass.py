class Account():
    def __init__(self, holder, number, balance,credit_line=1500): 
        self.Holder = holder 
        self.Number = number 
        self.Balance = balance
        self.CreditLine = credit_line

    def deposit(self, amount): 
        self.Balance += amount

    def withdraw(self, amount): 
        if(self.Balance - amount < -self.CreditLine):
            return False  
        else: 
            self.Balance -= amount 
            return True

    def balance(self): 
        self.Balance=balance
        print (balance)

    def transfer(self, target, amount):
        if(self.Balance - amount < -self.CreditLine):
            return False  
        else: 
            self.Balance -= amount 
            target.Balance += amount 
            return True
k = Account("Himan",345267,10000)
k.deposit(1000)
k.balance()
