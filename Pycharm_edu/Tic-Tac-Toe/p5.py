inp = list(("_"*9).replace("_", " "))
rows = [inp[0:3], inp[3:6], inp[6:9]]
cols = [inp[0:7:3], inp[1:8:3], inp[2:9:3]]
diags = [inp[0:9:4], inp[2:7:2]]


print("---------")
print("|", *rows[0], "|", sep=" ")
print("|", *rows[1], "|", sep=" ")
print("|", *rows[2], "|", sep=" ")
print("---------")

turn_X = True

while True:
    user = input("Enter the coordinates:").split()

    try:
        user = [int(x) for x in user]
    except:
        print("You should enter numbers!")
        continue

    if not (1 <= user[0] <= 3 and 1 <= user[1] <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    coor = (3-user[1], user[0]-1)  # cai nay quan trong

    if rows[coor[0]][coor[1]] != " ":
        print("This cell is occupied! Choose another one!")
        continue

    if turn_X:
        turn_X = False
        rows[coor[0]][coor[1]] = "X"
    else:
        turn_X = True
        rows[coor[0]][coor[1]] = "O"

    inp = [x for row in rows for x in row]
    cols = [inp[0:7:3], inp[1:8:3], inp[2:9:3]]
    diags = [inp[0:9:4], inp[2:7:2]]

    print("---------")
    print("|", *rows[0], "|", sep=" ")
    print("|", *rows[1], "|", sep=" ")
    print("|", *rows[2], "|", sep=" ")
    print("---------")

    x_count = len([x for row in rows for x in row if x == 'X'])
    o_count = len([o for row in rows for o in row if o == 'O'])

    if ['X', 'X', 'X'] in rows or ['X', 'X', 'X'] in cols or ['X', 'X', 'X'] in diags:
        print("X wins")
        break
    elif ['O', 'O', 'O'] in rows or ['O', 'O', 'O'] in cols or ['O', 'O', 'O'] in diags:
        print("O wins")
        break
    elif (x_count + o_count) == len(inp):
        print("Draw")
        break
