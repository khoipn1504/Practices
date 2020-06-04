import argparse
import math
from math import log, pow


def check_input(args):
    check = [args.type, args.principal,
             args.periods, args.interest, args.payment]
    count_input = sum(1 for i in check if i != None)

    if count_input < 4 or args.type == None or (args.type == "diff" and args.payment != None) or args.interest == None or any([i < 0 for i in check[1:]if i != None]):
        print("Incorrect parameters")
        return False
    return True


def count_of_months(args):
    p = args.principal
    a = args.payment
    i = args.interest/(12*100)

    n = math.ceil(log(a/(a-i*p), 1+i))

    year = n//12
    month = n-12*year

    if year == 0:
        print("You need {} months to repay this credit!".format(month))
    elif month == 0:
        print("You need {} years to repay this credit!".format(year))
    else:
        print("You need {} years and {} months to repay this credit!".format(
            year, month))

    print("Overpayment = {}".format(round(a*n-p)))


def annuity_monthly_payment(args):
    p = args.principal
    n = args.periods
    i = args.interest/(12*100)

    a = math.ceil(p*(i*pow(1+i, n)/(pow(1+i, n)-1)))

    print("Your annuity payment = {}!".format(a))
    print("Overpayment = {}".format(round(a*n-p)))


def credit_principal(args):
    a = args.payment
    n = args.periods
    i = args.interest/(12*100)

    p = round(a/(i*pow(1+i, n)/(pow(1+i, n)-1)))

    print("Your credit principal = {}!".format(p))
    print("Overpayment = {}".format(round(a*n-p)))


def diff_payment(args, month):
    i = args.interest/1200
    d = (args.principal/args.periods)+(i *
                                       (args.principal-args.principal*(month-1)/args.periods))
    print("Month {}: paid out {}".format(month, math.ceil(d)))
    return math.ceil(d)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type")
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--payment", type=int)
    args = parser.parse_args()

    if check_input(args):
        if args.type == "diff":
            total = 0
            for i in range(1, args.periods+1):
                total += diff_payment(args, i)
            print("\nOverpayment = {}".format(round(total-args.principal)))
        elif args.type == "annuity":
            if args.principal == None:
                credit_principal(args)
            elif args.periods == None:
                count_of_months(args)
            elif args.payment == None:
                annuity_monthly_payment(args)
