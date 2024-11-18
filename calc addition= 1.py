while exit != "Q":
    a = input("place first value:")
    operation = input ("place operation \"-\" or \"+\"")
    print (a+operation)
    b = input("place second value: ")
    print (a + operation + b)
    c = 0
    if operation == "+":
        c = int(a) + int(b)
    elif operation == "-":
        c = int(a) - int(b)
    else:
        print ("wrong operation")
    print (a + operation + b + "=" + str(c) )
    exit = input ("press \"Q\" to exit")
