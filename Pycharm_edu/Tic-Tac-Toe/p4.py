inp = list('X_X_O____')
rows = [inp[0:3], inp[3:6], inp[6:9]]
cols = [inp[0:7:3], inp[1:8:3], inp[2:9:3]]
diags = [inp[0:9:4], inp[2:7:2]]


print("---------")
print("|", *rows[0], "|", sep=" ")
print("|", *rows[1], "|", sep=" ")
print("|", *rows[2], "|", sep=" ")
print("---------")


user = input("Enter the coordinates:").split()

try:
    user = [int(x) for x in user]
except:
    print("You should enter numbers!")
    continue

if not (1 <= user[0] <= 3 and 1 <= user[1] <= 3):
    print("Coordinates should be from 1 to 3!")
    continue

coor = (3-user[0], user[1]-1)

if rows[coor[0]][coor[1]] != "_" and rows[coor[0]][coor[1]] != " ":
    print("This cell is occupied! Choose another one!")
    continue

rows[coor[0]][coor[1]] = "X"
print("---------")
print("|", *rows[0], "|", sep=" ")
print("|", *rows[1], "|", sep=" ")
print("|", *rows[2], "|", sep=" ")
print("---------")


# x_count = len([x for x in inp if x == 'X'])
# o_count = len([o for o in inp if o == 'O'])


# if (x_count - o_count >= 2 or o_count - x_count >= 2) or (['X', 'X', 'X'] in rows or ['X', 'X', 'X'] in cols or ['X', 'X', 'X'] in diags) and (['O', 'O', 'O'] in rows or ['O', 'O', 'O'] in cols or ['O', 'O', 'O'] in diags):
#     print("Impossible")
# elif ['X', 'X', 'X'] in rows or ['X', 'X', 'X'] in cols or ['X', 'X', 'X'] in diags:
#     print("X wins")
# elif ['O', 'O', 'O'] in rows or ['O', 'O', 'O'] in cols or ['O', 'O', 'O'] in diags:
#     print("O wins")
# elif (x_count + o_count) < len(inp):
#     print("Game not finished")
# else:
#     print("Draw")
