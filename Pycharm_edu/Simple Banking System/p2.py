import random


class Card:
    """Bank card data model"""
    id = 0
    number = ''
    pin = ''
    balance = 0


class Account(Card):

    def __init__(self):
        self.id = random.randint(10000000, 99999999)
        temp = str(400000000000000+self.id)
        self.number = temp + self.__luhn(temp)
        self.pin = ''.join(map(str, random.sample(range(0, 9), 4)))

    def __luhn(self, temp):
        list_check = list(map(int, list(temp)))
        check_sum = 0
        for idx, value in enumerate(list_check):
            if idx % 2 == 0:
                list_check[idx] = value*2
            if list_check[idx] > 9:
                list_check[idx] -= 9
            check_sum += list_check[idx]
        return str(10 - int(str(check_sum)[-1]))


class Menu:
    """Menu of the program"""

    def __init__(self):
        self.__choice = '0'

    def __repr__(self):
        return self.__choice

    def __eq__(self, other):
        return True if self.__choice == other else False

    @staticmethod
    def __show_main_menu():
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')

    @staticmethod
    def __show_account_menu():
        print('1. Balance')
        print('2. Log out')
        print('0. Exit')

    def show_and_get_choice(self):
        if self.__choice.startswith('2'):
            self.__show_account_menu()
            self.__choice = f'{self.__choice[0]}.{input()}'
        else:
            self.__show_main_menu()
            self.__choice = input()

    def back_to_main(self):
        self.__choice = '0'


class Banking:
    """Banking system"""

    def __init__(self):
        self.menu = Menu()
        self.current_account = None
        self.accounts = {}  # temporary dict (database) for accounts

    def create_account(self):
        """Creates a customer account"""
        account = Account()
        self.accounts[account.id] = account  # temporary solution
        # show the result according to the condition of the task
        print('Your card has been created')
        print('Your card number:')
        print(f'{self.accounts[account.id].number}')
        print('Your card PIN:')
        print(f'{self.accounts[account.id].pin}\n')

    def login(self):
        print('Enter your card number:')
        number = input()
        print('Enter your PIN:')
        pin = input()
        # check the correctness of the entered data
        for account in self.accounts.values():
            if account.number == number:
                if account.pin == pin:
                    print('You have successfully logged in!\n')
                    self.current_account = account
                    return
        print('Wrong card number or PIN!\n')
        self.menu.back_to_main()

    def show_balance(self):
        """Shows client balance"""
        print(f'Balance: {self.current_account.balance}\n')

    def log_out(self):
        """Shows the main menu, allowing the client to log in with another account."""
        print('You have successfully logged out!\n')
        self.menu.back_to_main()

    def run(self):
        """Main logic of the program"""
        while True:
            self.menu.show_and_get_choice()
            # fulfill the wishes of the client
            if self.menu == '1':
                self.create_account()
            elif self.menu == '2':
                self.login()
            elif self.menu == '2.1':
                self.show_balance()
            elif self.menu == '2.2':
                self.log_out()
            else:
                print('Bye!')
                break


if __name__ == '__main__':
    banking = Banking()
    banking.run()
