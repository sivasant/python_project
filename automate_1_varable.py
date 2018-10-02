def password():
    print("Hi How are you?")
    while True:
        print("Whats your name?")
        myName = input()
        print('It is good to meet you, ' + myName)
        print('Please enter your password')
        password = input()
        if password == 'kothi' :
            print('Access Granted')
            break
        else:
            print('Access Denied')
            continue
        
def collatz():
    print('Please enter the number')
    number = int(input())
    if number % 2 == 0:
        return number // 2
    else:
        return (3*number + 1)
    
#password()
print("Please continue")
while True:
    if collatz() == 1:
        break
    else:
        continue