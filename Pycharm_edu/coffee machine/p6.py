
class CoffeeMachine():

    def __init__(self, water, milk, coffee, cup, money):
        self.material = {
            'water': water,
            'milk': milk,
            'coffee': coffee,
            'cup': cup,
            'money': money,
        }

        self.type_coffee = {
            'espresso': {
                'water': 250,
                'coffee': 16,
                'money': -4,
                'cup': 1,
            },
            'latte': {
                'water': 350,
                'milk': 75,
                'coffee': 20,
                'money': -7,
                'cup': 1,
            },
            'cappuccino': {
                'water': 200,
                'milk': 100,
                'coffee': 12,
                'money': -6,
                'cup': 1,
            },
        }

    def show_machine_state(self):
        print()
        print('''The coffee machine has:
{water} of water
{milk} of milk
{coffee} of coffee beans
{cup} of disposable cups
${money} of money'''.format(**self.material))
        print()

    def fill(self):
        print()
        self.material['water'] += int(
            input("Write how many ml of water do you want to add:\n"))
        self.material['milk'] += int(
            input("Write how many ml of milk do you want to add:\n"))
        self.material['coffee'] += int(
            input("Write how many grams of coffee beans do you want to add:\n"))
        self.material['cup'] += int(
            input("Write how many disposable cups of coffee do you want to add:\n"))
        print()

    def take(self):

        print()
        print("I gave you ${}".format(self.material['money']))
        print()
        self.material['money'] = 0

    def check_material(self, coffee_name):
        check = {
            key: self.material[key] - self.type_coffee[coffee_name].get(key, 0) for key in self.material}
        for key, value in check.items():
            if value < 0:
                a = ''
                if key == 'water':
                    a = 'water'
                elif key == 'coffee':
                    a = 'coffee beans'
                elif key == 'milk':
                    a = 'milk'
                elif key == 'cup':
                    a = 'cup'
                elif key == 'cup':
                    a = 'disposable cups'
                print('Sorry, not enough %s!' % (a))
                return False
            else:
                print('I have enough resources, making you a coffee!')
                return True

    def buy(self):
        choice = input(
            'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')

        if choice == '1':
            if self.check_material('espresso'):
                self.material = {
                    key: self.material[key] - self.type_coffee['espresso'].get(key, 0) for key in self.material}
        elif choice == '2':
            if self.check_material('latte'):
                self.material = {
                    key: self.material[key] - self.type_coffee['latte'].get(key, 0) for key in self.material}
        elif choice == '3':
            if self.check_material('cappuccino'):
                self.material = {
                    key: self.material[key] - self.type_coffee['cappuccino'].get(key, 0) for key in self.material}


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)


while True:
    action = input('Write action (buy, fill, take, remaining, exit):\n')
    if action == 'buy':
        coffee_machine.buy()
    elif action == 'fill':
        coffee_machine.fill()
    elif action == 'take':
        coffee_machine.take()
    elif action == 'remaining':
        coffee_machine.show_machine_state()
    elif action == 'exit':
        break
