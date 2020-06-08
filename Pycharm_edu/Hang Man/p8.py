import random
from string import ascii_lowercase

print("H A N G M A N")
while True:
    mode = input('Type "play" to play the game, "exit" to quit: ')
    if mode == 'exit':
        break
    elif mode == "play":
        print()

        question = ['python', 'java', 'kotlin', 'javascript']
        pick = question[random.randint(0, len(question)-1)]
        check_char = set(pick)

        show = len(pick)*"-"

        inp_history = set()
        count = 0
        while True:
            if count == 8:
                print("You are hanged!")
                break
            else:
                print()
                print(show)
                ans = input("Input a letter: ")

                if len(ans) > 1 or len(ans) == 0:
                    print("You should input a single letter")
                    continue
                if ans in inp_history:
                    print("You already typed this letter")
                    continue
                if ans not in ascii_lowercase:
                    print("It is not an ASCII lowercase letter")
                    continue

                inp_history.add(ans)

                if ans in set(show):
                    count += 1
                    print("No improvements")
                elif ans in check_char:
                    copy = show
                    show = ""
                    for i in range(len(pick)):
                        if pick[i] == ans:
                            show += ans
                        elif copy[i] != "-":
                            show += copy[i]
                        else:
                            show += "-"
                else:
                    count += 1
                    print("No such letter in the word")

                # check win
                if show == pick:
                    print(show)
                    print("You guessed the word!")
                    print("You survived!")
                    break
