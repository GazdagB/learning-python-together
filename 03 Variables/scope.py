
x = "awesome"

def myfunc():
    print("Python is " + x)    
    

myfunc()

def myfunc2():
    global x
    x = "fantastic"
    print("Python is " + x)
    
myfunc2()