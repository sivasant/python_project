# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:02:26 2018

@author: siva santhosh
"""
import os
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
        print(os.path.join('C:\\Users\\sivasanthosh', filename))


calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath))
print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
print(os.listdir('C:\\Windows\\System32'))
