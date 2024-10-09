import sys

params = sys.argv[1:]

if len(params) < 2:
    print("none")
else:
    for Rparam in reversed(params):
        print(Rparam)
