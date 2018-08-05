def example():
    print('basic function')
    z=3+9
    print(z)

#Function with parameter    
def add(a,b):
    c=a+b
    print('the result is',c)

add(5,3)
add(a=3,b=5)

#Function with default parameters
def add_new(a,b=6):
    print(a,b)

add_new(2)

def basic_window(width,height,font='TNR',bgc='w',scrollbar=True):
    print(width,height,font,bgc)

basic_window(500,350,bgc='a')

