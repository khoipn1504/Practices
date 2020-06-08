import random

print("H A N G M A N")
question = ['python', 'java', 'kotlin', 'javascript']
pick = question[random.randint(0, len(question)-1)]
show=pick[:3]+(len(pick)-3)*"-"
ans = input("Guess the word {}: ".format(show))
if ans == pick:
    print("You survived!")
else:
    print("You are hanged!")
