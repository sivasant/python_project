text = 'Simpletext to save\nNew line!'
saveFile = open('example.txt','w')

saveFile.write(text)

saveFile.close()

appending = 'My name is santhosh\n Raj'
saveFile = open('example.txt','a')
saveFile.write(appending)
saveFile.close()


reading = open('example.txt','r').read()
readingLines = open('example.txt','r').readlines()
print(reading)
print(readingLines)
