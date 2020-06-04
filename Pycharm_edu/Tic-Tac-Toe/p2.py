inp = input("Enter cells: ")
rows = [inp[0:3], inp[3:6], inp[6:9]]
cols = [inp[0:7:3], inp[1:8:3], inp[2:9:3]]
diags = [inp[0:9:4], inp[2:7:2]]


print("---------")
print("|", *rows[0], "|", sep=" ")
print("|", *rows[1], "|", sep=" ")
print("|", *rows[2], "|", sep=" ")
print("---------")
