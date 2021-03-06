def show_machine_state(water, milk, coffee, cup, money):
    print('''The coffee machine has:
%i of water
%i of milk
%i of coffee beans
%i of disposable cups
%i of money''' % (water, milk, coffee, cup, money))
    print()


def buy():
    choice = input(
        'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
    type_coffee = {
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

    global material

    if choice == '1':
        material = {
            key: material[key] - type_coffee['espresso'].get(key, 0) for key in material}
    elif choice == '2':
        material = {
            key: material[key] - type_coffee['latte'].get(key, 0) for key in material}
    elif choice == '3':
        material = {
            key: material[key] - type_coffee['cappuccino'].get(key, 0) for key in material}


def fill():
    global material

    material['water'] += int(
        input("Write how many ml of water do you want to add:\n"))
    material['milk'] += int(
        input("Write how many ml of milk do you want to add:\n"))
    material['coffee'] += int(
        input("Write how many grams of coffee beans do you want to add:\n"))
    material['cup'] += int(
        input("Write how many disposable cups of coffee do you want to add:\n"))
    print()


def take():
    global material

    print("I gave you %i" % (material['money']))
    print()
    material['money'] = 0


# init variable
material = {
    'water': 400,
    'milk': 540,
    'coffee': 120,
    'cup': 9,
    'money': 550,
}

while True:
    show_machine_state(**material)
    action = input('Write action (buy, fill, take):\n')
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
