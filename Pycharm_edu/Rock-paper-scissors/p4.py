import random

user_name = input('Enter your name: ')
print('Hello, {}'.format(user_name))
user_score = 0

file_rate = open('rating.txt', 'r')
for line in file_rate:
    if user_name in line.split():
        user_score = int(line.split()[1])
        break
file_rate.close()


while True:
    user = input()
    if user == '!exit':
        print("Bye!")
        break
    elif user == '!rating':
        print('Your rating:', user_score)
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
            user_score += 100
            print("Well done. Computer chose {} and failed".format(computer))
        elif rule[user][computer] == 'lose':
            print("Sorry, but computer chose {}".format(computer))
        else:
            user_score += 50
            print("There is a draw ({})".format(user))
