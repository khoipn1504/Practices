import random

print("H A N G M A N")
print()

question = ['python', 'java', 'kotlin', 'javascript']
pick = question[random.randint(0, len(question)-1)]
check_char = set(pick)

show = len(pick)*"-"

count = 0
while True:
    if count == 8:
        print("Thanks for playing!")
        print("We'll see how well you did in the next stage")
        break
    else:
        print(show)
        ans = input("Input a letter: ")
        if ans in check_char:
            show = ""
            for i in range(len(pick)):
                if pick[i] == ans:
                    show += ans
                else:
                    show += "-"
            count += 1
        else:
            count += 1
            print("No such letter in the word")
        print()
