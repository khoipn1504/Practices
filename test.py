
def high_and_low(numbers):
  n = map(int, numbers.split(' '))
  return str(max(n)) + ' ' + str(min(n))

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))