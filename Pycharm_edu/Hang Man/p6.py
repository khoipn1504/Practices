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
        print("You are hanged!")
        break
    else:
        print()
        print(show)
        ans = input("Input a letter: ")
        inp_history.add(ans)

        if ans in set(show):
            count += 1
            print("No improvements")
        elif ans in check_char:
            show = ""
            for i in range(len(pick)):
                if pick[i] == ans:
                    show += ans
                else:
                    show += "-"
        else:
            count += 1
            print("No such letter in the word")

        if show == pick:
            print(show)
            print("You guessed the word!")
            print("You survived!")
            break
