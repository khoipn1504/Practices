import random

user = input()
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
