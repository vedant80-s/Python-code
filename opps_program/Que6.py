# Question 6
class BankAccount:
    def __init__(self , account_holder , balance , password):
        self.__password = password
        self.account_holder = account_holder
        self.__balance = balance

    def get_balance(self , password):
        return self.__balance if password == self.__password else "Wrong Password"

    def set_password(self , old_pass , new_pass):
        self.__password  = new_pass if old_pass == self.__password else "Wrong Old Password"
        return self.__password 
    
    def get_account_holder(self):
        return self.account_holder

ba = BankAccount('Ravi' , 34000 , 'Ravi')
print(ba.get_balance('Ravi')) 
print(ba.get_balance('Rav'))
print(ba.get_account_holder()) 
print(ba.set_password('Ravi' , 'Rav')) 
print(ba.set_password('Ravi' , 'Rav')) 