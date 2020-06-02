water = int(input('Write how many ml of water the coffee machine has:\n'))
milk = int(input('Write how many ml of milk the coffee machine has:\n'))
coffee = int(
    input('Write how many grams of coffee beans the coffee machine has:\n'))
cups = int(input('Write how many cups of coffee you will need:\n'))

check = (water//200, milk//50, coffee//15)
if cups == min(check):
    print('Yes, I can make that amount of coffee')
elif cups < min(check):
    print("Yes, I can make that amount of coffee (and even %i more than that)" % (
        min(check)-cups))
else:
    print("No, I can make only %i cup(s) of coffee" % (min(check)))
