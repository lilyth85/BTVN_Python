from datetime import date

class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self._name = name
        self._date_of_birth = date_of_birth
        self._email = email
        self._phone = phone
    
    def get_info(self):
        return [self._name, self._date_of_birth, self._email, self._phone]

class BankAccount:
    def __init__(self, account_number, account_name, owner, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self.balance = balance
        self._owner = owner

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(f"Số tài khoản khách hàng là: {self._account_number}")
        print(f"Thông tin khách hàng như sau:")
        print(
                f"-- Tên khách hàng: {self._owner.get_info()[0]}", 
                f"-- DOB: {self._owner.get_info()[1]}",
                f"-- email: {self._owner.get_info()[2]}",
                f"-- phone: {self._owner.get_info()[3]}",
                f"Số dư là:{self.balance}",
                "====================================",
                sep = '\n')
        # print(f"-- DOB: {self._owner.get_info()[1]}")
        # print(f"-- email: {self._owner.get_info()[2]}")
        # print(f"-- phone: {self._owner.get_info()[3]}")
        # print(f"Số dư là:{self.balance}")
        # print("==========================")
            
class SavingAccount(BankAccount):
    def __init__(self,account_number, account_name, owner, balance, monthly_interest_rate = 0.005):
        super().__init__(account_number, account_name, owner, balance)
        self._monthly_interest_rate = monthly_interest_rate
    
    def calculate_interest(self):
        interest_money = self._balance * self._monthly_interest_rate
        return interest_money
    


huyenpt = Customer("PHAM THI HUYEN","30/01/20009"huyenpt@gmail.com","089xx")
huyenpt_bank = BankAccount("8888","huyenpt acc name", huyenpt, 1000)
huyenpt_bank.display()
huyenpt_bank_interest = SavingAccount("8889","huyenpt account name", huyenpt, 3000000)
huyenpt_bank_interest.display()
print(f"Tiền lãi hàng tháng dự tính: {huyenpt_bank_interest.calculate_interest()}")
