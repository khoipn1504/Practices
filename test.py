import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-ans",
                    "--ans", help="display a square of a given number", action="store_true")
args = parser.parse_args()
print(args.ans**2)
