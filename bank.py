class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def UpLoadMoney(self,amount):
        self.balance += amount
        print( f"You Up Load ${amount}, and now you have ${self.balance}")


    def DownloadMoney(self,amount):
        if amount > self.balance:
            print("Sorry, unfortunately you don´t have enough money in your account ")
        else:
            self.balance -= amount
            print(f"You download ${amount}, and now you have ${self.balance}")


class SavingAccount(BankAccount):
    def __init__(self, balance,min_balance):
        super().__init__(balance)
        self.min_balance = min_balance


    def DownloadMoney(self, amount):
        if self.balance - amount < self.min_balance:
            print (f"You can´t download money, because you need to have ${self.min_balance} in your account")
        else:
            self.balance -= amount
            print (f"You download ${amount}, you new balance is ${self.balance}")


account=SavingAccount(1000,200)
account.UpLoadMoney(500)
account.DownloadMoney(1300)
account.DownloadMoney(100)