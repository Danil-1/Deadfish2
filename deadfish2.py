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
        a += 1 #Increase Accumulator

    elif inp == "d":
        a -= 1 #Decrease

    elif inp == "s":
        a *= a #Square

    elif inp == "o":
        print(a) #output

    elif inp == "O":
        print(b) #print string

    elif inp == "n":
        a = 0 #Reset

    elif inp == 'c':
        print(chr(a)) #print char value

    elif inp == 'h':
        exit #Halt

    elif inp == 'r':
        b = input(">> ") #Input
    elif input == 'de':
        a=a+0.1 #Garbage(?)
def parse(cmd):
    do(cmd)

def read(cmd):
    tokens = list(cmd)
    for i in range(0, len(tokens)):
        parse(tokens[i])

while 1:
    read(input("> "))
