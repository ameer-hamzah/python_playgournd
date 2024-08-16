class NewBankAccount:
    defalutID = 1 # Class attribute
    
    def __init__(self, name, type, balance):
        self.name = name
        self.type = type
        self.balance = balance
        self.accountNumber = NewBankAccount.defalutID
        NewBankAccount.defalutID += 1
        
    def deposit(self, amount):
        print("Deposited Amount: ", amount)
        self.balance += amount
        print("New Balance: ", self.balance)
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not Enough Money...!")
        else:
            self.balance -= amount
            print("Remaining Balance: ", self.balance)
        
    def getBalance(self):
        return print("Current Balance: ", self.balance)
    
    def getDetails(self):
        print("Customer Name: ", self.name)
        print("Account Type: ", self.type)
        print("Current Balance: ", self.balance)
        print("Account Number: ", self.accountNumber)
    
    # def withdraw(self, amount):
    #     self.balance -+ amount

if __name__ == '__main__':
    # user1 = NewBankAccount('Akram', 'Current', 3000)
    # user1.getBalance()
    # user1.deposit(1500)
    # user1.getDetails()
    
    user2 = NewBankAccount('Alam', 'Savings', 1000)
    user2.getBalance()
    # user2.deposit(1500)
    user2.getDetails()
    user2.withdraw(3000)
    
    
        