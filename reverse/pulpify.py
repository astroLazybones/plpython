import sys

if len(sys.argv) <= 1:
    print("Not enough files specified")
    sys.exit(1)

f = open(sys.argv[1], "r")
print(f.read()[::-1])
