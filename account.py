class Account:
    '''
    A class hosting methods to deposit or withdraw from a balance
    as well as get the current balance and account name
    '''
    def __init__(self, name: str, balance=0) -> None:
        '''
        Constructor to create class variables holding the balance and name
        :param name: the name of the account
        :param balance: the value of the balance in the account
        '''
        self.account_name = name
        self.account_balance = balance

    def deposit(self, amount: float) -> bool:
        '''
        a method to deposit a value into the class variable balance
        :param amount: the amount being deposited into the account
        :return: Boolean value to determine if a balance was added to the account
        '''
        if amount <= 0:
            return False
        else:
            self.account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        '''
        a method to withdraw an amount from the class variable balance
        :param amount: the amount to withdraw from the account
        :return: Boolean value to determine if a value was withdrawn from the balance
        '''
        if amount <= 0:
            return False
        elif amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def get_balance(self) -> float:
        '''
        a method to check the balance of an account
        :return: the value of the account balance
        '''
        return self.account_balance

    def get_name(self) -> str:
        '''
        a method to check the name of an account
        :return: the name of the account
        '''
        return self.account_name
