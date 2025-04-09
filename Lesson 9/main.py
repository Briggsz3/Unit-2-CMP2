class BankAccount:
    __num_transactions = 0 # class variable
    def __init__(self, name, number, balance, ):
        self.name = name
        self.number = number
        self.__balance = balance
    
    def get_balance(self):
        return f"${self.__balance:.2f}"
    
    def get_num_transactions(self):
        return BankAccount.__num_transactions
    
    # setter method

    def set_balance(self, amount):
        if amount > 0:
            self.__balance+=amount
            BankAccount.__num_transactions += 1


    
my_account = BankAccount("Zach", 3483, 100000)
# print(my_account.__balance) # Won't be able to print out the balance. Doesn't allow for any modifications (pre get_balance)
print(my_account.get_balance())
print(my_account.get_num_transactions())
my_account.set_balance(100)
print(my_account.get_balance())
print(my_account.get_num_transactions())
