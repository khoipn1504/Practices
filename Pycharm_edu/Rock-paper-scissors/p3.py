import random


while True:
    user = input()
    if user == '!exit':
        print("Bye!")
        break
    elif user != 'rock' and user != 'scissors' and user != 'paper':
        print('Invalid input')
    else:
        option = ['rock', 'scissors', 'paper']
        computer = random.choice(option)

        rule = {
            'rock': {
                'scissors': 'win',
                'paper': 'lose',
                'rock': 'draw'
            },
            'scissors': {
                'paper': 'win',
                'rock': 'lose',
                'scissors': 'draw'
            },
            'paper': {
                'rock': 'win',
                'scissors': 'lose',
                'paper': 'draw'
            },
        }

        if rule[user][computer] == 'win':
            print("Well done. Computer chose {} and failed".format(computer))
        elif rule[user][computer] == 'lose':
            print("Sorry, but computer chose {}".format(computer))
        else:
            print("There is a draw ({})".format(user))
