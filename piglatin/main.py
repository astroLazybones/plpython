import sys

#Encode: 
def ency(code):
    code = code.replace("\n", ";")
    code = code.split()
    final_code = ""
    d = ""
    for i in code:
        d = i[1:]+i[0] + "ay "
        final_code = final_code + d + " "
    return final_code

#Decode:
def decy(code):
    code = code.replace("ay ", " ")
    code = code.split()
    final_code = ""
    for i in code:
        d = i[-1]+i[:-1]
        final_code = final_code + d + " "
    final_code = final_code.replace(";", "\n")
    return final_code

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Not enough files specified")
        sys.exit(1)
    if "-c" in sys.argv:
        comm = ""
        for line in sys.stdin:
            comm = comm + line + "\n"
        exec(decy(comm))
        sys.exit(0)
    f = open(sys.argv[1], "r")
    runcode = decy(f.read())
    exec(runcode)
