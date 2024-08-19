import sys

if len(sys.argv) <= 1:
    print("Not enough files specified")
    sys.exit(1)
if "-c" in sys.argv:
    comm = ""
    for line in sys.stdin:
        comm = comm + line + "\n"
    exec(comm[::-1])
    sys.exit(0)
f = open(sys.argv[1], "r")
runcode = f.read()[::-1]
exec(runcode)
