class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    
    def __init__(self):
        pass

acc = Account(1000,12345)

print(acc.account_no)
print(acc.balance)