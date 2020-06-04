import math

credit = int(input("Enter the credit principal:\n"))
action = input(
    "What do you want to calculate?\ntype 'm' - for count of months,\ntype 'p' - for monthly payment:")

if action == "m":
    monthly_pay = int(input("Enter monthly payment:\n"))
    month_count = math.ceil(credit/monthly_pay)
    print("It takes {} month to repay the credit".format(month_count))
elif action == "p":
    month_count = int(input("Enter count of months:\n"))
    monthly_pay = math.ceil(credit/month_count)
    last_pay = credit-(month_count-1)*monthly_pay
    if last_pay != monthly_pay:
        print("Your monthly payment = {} with last month payment = {}.".format(
            monthly_pay, last_pay))
    else:
        print("Your monthly payment = {}".format(monthly_pay))
