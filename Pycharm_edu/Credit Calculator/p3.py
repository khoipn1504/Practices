import math
from math import log, pow


def count_of_months():
    p = int(input("Enter credit principal:\n"))
    a = float(input("Enter monthly payment:\n"))
    i = float(input("Enter credit interest:\n"))/(12*100)

    n = math.ceil(log(a/(a-i*p), 1+i))

    year = n//12
    month = n-12*year

    if year == 0:
        print("You need {} months to repay this credit!\n".format(month))
    elif month == 0:
        print("You need {} years to repay this credit!\n".format(year))
    else:
        print("You need {} years and {} months to repay this credit!\n".format(
            year, month))


def annuity_monthly_payment():
    p = int(input("Enter credit principal:\n"))
    n = int(input("Enter count of periods:\n"))
    i = float(input("Enter credit interest:\n"))/(12*100)

    a = math.ceil(p*(i*pow(1+i, n)/(pow(1+i, n)-1)))

    print("Your annuity payment = {}!\n".format(a))


def credit_principal():
    a = float(input("Enter monthly payment:\n"))
    n = int(input("Enter count of periods:\n"))
    i = float(input("Enter credit interest:\n"))/(12*100)

    p = round(a/(i*pow(1+i, n)/(pow(1+i, n)-1)))

    print("Your credit principal = {}!\n".format(p))


if __name__ == "__main__":

    while True:

        action = input(
            "What do you want to calculate?\ntype 'n' - for count of months,\ntype 'a' - for monthly payment:\ntype 'p' - for credit principal:\n")

        if action == 'n':
            count_of_months()
        elif action == 'a':
            annuity_monthly_payment()
        elif action == 'p':
            credit_principal()

        break
