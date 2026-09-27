# Bank management system
from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self,acc_Num,name,balance):
        self.acc_Num = acc_Num
        self.name = name
        self.__balance = balance
    def get__balance(self):
        return self.__balance
    def add_balance(self,amount):
        self.__balance += amount
    def subtract_balance(self,amount):
        self.__balance -= amount
    def account_details(self):
        print("Account number =",self.acc_Num)
        print("Person name =",self.name)
        print("Balance =",self.get__balance())
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class SavingAccount(BankAccount):
    def deposit(self,amount):
        if amount > 0:
            self.add_balance(amount)
            print("Deposit successful")
            print("New balance =",self.get__balance())
        else:
            print("Invalid amount")
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.get__balance():
            print("Insufficient balance")
        else:
            self.subtract_balance(amount)
            print("Withdraw successful")
            print("Remaining balance =",self.get__balance())
        
s = SavingAccount(101,"Akshada",5000)
while True:
 choice = input("Enter choice: ")
 if choice == "1":
    amount = int(input("Enter amount: "))
    s.deposit(amount)
 elif choice == "2":
    amount = int(input("Enter amount: "))
    s.withdraw(amount)
 elif choice == "3":
    print("Balance =", s.get__balance())
 elif choice == "4":
        s.account_details()
 elif choice == "5":
    print("Thank you!")
    break
 else:
     print("Invalid choice")
