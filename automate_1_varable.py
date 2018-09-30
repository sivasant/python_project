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