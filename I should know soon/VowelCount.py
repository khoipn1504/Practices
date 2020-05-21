def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")

def getCount1(inputStr):
    return sum(c in 'aeiou' for c in inputStr)

inputStr='i miss you bitch'

print(getCount1(inputStr))
