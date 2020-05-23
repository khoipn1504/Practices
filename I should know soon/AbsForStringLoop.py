def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    space = n//2
    ans = ''
    for i in range(n):
        ans += ' '*abs(space)
        ans += '*'*(n-2*abs(space))
        ans += '\n'
        space -= 1
    print(ans)


diamond(5)
