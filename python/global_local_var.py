x=6

def sant():
    print(x)

sant()

def sant_overwrite():
    global x
    x+=5
    print(x)

sant_overwrite()
