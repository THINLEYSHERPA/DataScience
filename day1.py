class Bank:
    def __init__(self,first_name,last_name,age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__balance = 0
    def get_balance(self):
        return self.__balance
    def deposit(self,deposit_amt):
        if deposit_amt < 0:
            print ('invalid amount')
        else:
            return 
        self.__balance += deposit_amt
    def withdrew(self,with_amt):
        if with_amt > self.__balance:
            print('insuffecent amount')
        elif with_amt < 
        