import random

print("H A N G M A N")
question = ['python', 'java', 'kotlin', 'javascript']
pick = question[random.randint(0, len(question)-1)]

ans = input("Guess the word: ")
if ans == pick:
    print("You survived!")
else:
    print("You are hanged!")
