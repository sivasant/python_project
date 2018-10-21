# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 22:02:29 2018

@author: siva santhosh
"""

#TIC TAC TOE GAME BY SANTHOSH"

tic_tac_toe_board= {'top_L' : '','top_M':'','top_R':'',
      'Mid_L' : '','Mid_M' : '','Mid_R' : '',
      'Bottom_L'  : '','Bottom_M' : '','Bottom_R' : ''}

def print_tic_tac_toe_board(board):
    print(board['top_L']+ ' |'+board['top_M']+ ' |'+board['top_R'])
    print('-+-+-')
    print(board['Mid_L'] + ' |' + board['Mid_M'] + ' |' + board['Mid_R'])
    print('-+-+-')
    print(board['Bottom_L'] + ' |' + board['Bottom_M'] + ' |' + board['Bottom_R'])
    
    
turn = 'x'
for i in range(9):
    print_tic_tac_toe_board(tic_tac_toe_board)
    print('Enter the move '+ turn+ ' Where do you want to put the move')
    move = input()
    tic_tac_toe_board[move]=turn
    if turn == 'x':
            turn = 'o'
    else:
            turn = 'x'
print_tic_tac_toe_board(tic_tac_toe_board)
    
