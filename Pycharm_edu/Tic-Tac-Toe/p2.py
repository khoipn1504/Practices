ans = '_XO__X___'
print("---------")
for i in range(0, 7, 3):
    print("| ", end="")
    print(' '.join(ans[i:i+3]), end='')
    print(" |")
print("---------")
