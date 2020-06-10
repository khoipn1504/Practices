import random

user_name = input('Enter your name: ')
print('Hello, {}'.format(user_name))

option = input().split(',')
if option == ['']:
    option = ['rock', 'scissors', 'paper']

rule = ('rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf',
        'sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun')

print("Okay, let's start")

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
    elif user not in option:
        print('Invalid input')
    else:
        index = rule.index(user)
        new_rule = rule[index:]+rule[:index]

        computer = random.choice(option)
        if computer in new_rule[1:8]:
            user_score += 100
            print("Well done. Computer chose {} and failed".format(computer))
        elif computer == user:
            user_score += 50
            print("There is a draw ({})".format(user))
        else:
            print("Sorry, but computer chose {}".format(computer))
