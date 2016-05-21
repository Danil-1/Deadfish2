a = 0
b = ""
skipping = False
reading = False
ifThis = []

def do(inp):
    global a
    global b
    global skipping
    global reading
    global ifThis
    
    if inp == "i":
        a += 1

    elif inp == "d":
        a -= 1

    elif inp == "s":
        a *= a

    elif inp == "o":
        print(a)

    elif inp == "O":
        print(b)

    elif inp == "n":
        a = 0

    elif inp == 'c':
        print(chr(a))

    elif inp == 'h':
        exit

    elif inp == 'r':
        b = input(">> ")

def parse(cmd):
    do(cmd)

def read(cmd):
    tokens = list(cmd)
    for i in range(0, len(tokens)):
        parse(tokens[i])

while 1:
    read(input("> "))
