class CreditCard():

    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        self._balance -= amount


if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('Khanh Map', 'VCB', '2313 3244 4564 2134', 2500))
    wallet.append(CreditCard('Bob', 'ACB', '3254 2654 2122 6574', 3500))
    wallet.append(CreditCard('Khoi', 'SAC', '1234 5678 1234 6634', 5000))

    for val in range(1, 17):
        for i in range(3):
            wallet[i].charge(val*(i+1))

    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance()>100:
            wallet[c].make_payment(100)
            print('New balance = ',wallet[c].get_balance(),end='\n\n')


