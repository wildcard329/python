

def intro1():
    print('''
///////////////////////     |||||||||        ////|||||||\\\\
//////////////////////      |||||||||       ////|||||||||\\\\
       ||||||               |||||||||      ////           \\\\
       ||||||               |||||||||     ////            ||||
       ||||||               |||||||||    ////
       ||||||               |||||||||    ||||
       ||||||               |||||||||    ||||
       ||||||               |||||||||    ||||
       ||||||               |||||||||    ||||
       ||||||               |||||||||    ||||
       ||||||               |||||||||    \\\\
       ||||||               |||||||||     \\\\           ||||
       ||||||               |||||||||      \\\\          ////
       ||||||               |||||||||       \\\\||||||||////
       ||||||               |||||||||        \\\\||||||////
''')


def intro2():   
    print('''
///////////////////////     //|||||\\           ////||||||\\\\
///////////////////////    ///|||||\\\         ////||||||||\\\\
       ||||||             ////     \\\\       ////          \\\\
       ||||||            ////       \\\\     ////           ||||
       ||||||           ||||        ||||    ////    
       ||||||           ||||        ||||    ||||
       ||||||           ||||||||||||||||    ||||
       ||||||           ||||||||||||||||    ||||
       ||||||           ||||||||||||||||    ||||
       ||||||           ||||        ||||    ||||
       ||||||           ||||        ||||    \\\\
       ||||||           ||||        ||||     \\\\           ||||
       ||||||           ||||        ||||      \\\\          ////
       ||||||           ||||        ||||       \\\\||||||||////
       ||||||           ||||        ||||        \\\\||||||////
''')


def intro3():
    print('''
///////////////////////      ////||||\\\\       ///////////////////
///////////////////////     ////||||||\\\\      //////////////////
       ||||||              ////        \\\\     ||||
       ||||||             ////          \\\\    ||||
       ||||||             ||||          ||||    ||||
       ||||||             ||||          ||||    ||||
       ||||||             ||||          ||||    //////////////////
       ||||||             ||||          ||||    /////////////////
       ||||||             ||||          ||||    ||||
       ||||||             ||||          ||||    ||||
       ||||||             ||||          ||||    ||||
       ||||||             ||||          ||||    ||||
       ||||||             \\\\          ////    ||||
       ||||||              \\\\        ////     ||||
       ||||||               \\\\||||||////      \\\\\\\\\\\\\\\\\\
       ||||||                \\\\||||////        \\\\\\\\\\\\\\\\\\
''')


board0 = [' ', '1', '2', '3']
board1 = ['a', '-', '-', '-']
board2 = ['b', '-', '-', '-']
board3 = ['c', '-', '-', '-']

def game():
    won = False
    while not won:
        print(board0,'\n',board1,'\n',board2,'\n',board3)
        spot = input('Please select a spot on the board.')
        placement = input('Please place X or O.')
        if spot == 'a1' and placement == 'x':
            board1[1] = 'X'
        elif spot == 'a1' and placement == 'o':
            board1[1] = 'O'
        elif spot == 'a2' and placement == 'x':
            board1[2] = 'X'
        elif spot == 'a2' and placement == 'o':
            board1[2] = 'O'
        elif spot == 'a3' and placement == 'x':
            board1[3] = 'X'
        elif spot == 'a3' and placement == 'o':
            board1[3] = 'O'
        elif spot == 'b1' and placement == 'x':
            board2[1] = 'X'
        elif spot == 'b1' and placement == 'o':
            board2[1] = 'O'
        elif spot == 'b2' and placement == 'x':
            board2[2] = 'X'
        elif spot == 'b2' and placement == 'o':
            board2[2] = 'O'
        elif spot == 'b3' and placement == 'x':
            board2[3] = 'X'
        elif spot == 'b3' and placement == 'o':
            board2[3] = 'O'
        elif spot == 'c1' and placement == 'x':
            board3[1] = 'X'
        elif spot == 'c1' and placement == 'o':
            board3[1] = 'O'
        elif spot == 'c2' and placement == 'x':
            board3[2] = 'X'
        elif spot == 'c2' and placement == 'o':
            board3[2] = 'O'
        elif spot == 'c3' and placement == 'x':
            board3[3] = 'X'
        elif spot == 'c3' and placement == 'o':
            board3[3] = 'O'
        else:
            input('Please enter a valid option.')
#        if board1[1] == 'X' and board1[2] == 'X' and board1[3] == 'X':
#            won = True
#        elif board1[1] == 'O' and board1[2] == 'O' and board1[3] == 'O':
#            won = True
#        elif board1[1] == 'X' and board2[1] == 'X' and board3[1] == 'X':
#            won = True
#        elif board1[1] == 'O' and board2[1] == 'O' and board3[1] == 'O':
#            won = True
#        elif board1[1] == 'X' and board2[2] == 'X' and board3[3] == 'X':
#            won = True
#        elif board1[1] == 'O' and board2[2] == 'O' and board3[3] == 'O':
#            won = True
#        elif board2[1] == 'X' and board2[2] == 'X' and board2[3] == 'X':
#            won = True
#        elif board2[1] == 'O' and board2[2] == 'O' and board2[3] == 'O':
#            won = True
#        elif board3[1] == 'X' and board3[2] == 'X' and board3[3] == 'X':
#            won = True
#        elif board3[1] == 'O' and board3[2] == 'O' and board3[3] == 'O':
#            won = True
#        elif board3[1] == 'X' and board2[2] == 'X' and board1[3] == 'X':
#            won = True
#        elif board3[1] == 'O' and board2[2] == 'O' and board1[3] == 'O':
#            won = True
#        elif board1[3] == 'X' and board2[3] == 'X' and board3[3] == 'X':
#            won = True
#        elif board1[3] == 'O' and board2[3] == 'O' and board3[3] == 'O':
#            won = True
#        elif board1[2] == 'X' and board2[2] == 'X' and board3[2] == 'X':
#            won = True
#        elif board1[2] == 'O' and board2[2] == 'O' and board3[2] == 'O':
#            won = True
#        else:
#            input('The game was a draw.')
#            won = True
#    play = input('Would you like to play again? ')
#    if play == 'y' or play == 'yes':
#        game()

intro1()
input()
intro2()
input()
intro3()
input()
game()
