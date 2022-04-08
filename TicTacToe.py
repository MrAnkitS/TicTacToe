from IPython.display import clear_output
import random
def display_board(board):
    clear_output()
    
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    
def player_input():
    
    marker = 'wrong'
    
    while marker!='X' and marker!='O':
        
        marker = input("Player 1 : Do you want to be 'X' or 'O'? ").upper()
        if marker!='X' and marker!='O':
            print("Invalid Choice!")
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    
def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    
    return((board[1]==mark and board[2]==mark and board[3]==mark)or
    (board[4]==mark and board[5]==mark and board[6]==mark)or
    (board[7]==mark and board[8]==mark and board[9]==mark)or
    (board[1]==mark and board[4]==mark and board[7]==mark)or
    (board[2]==mark and board[5]==mark and board[8]==mark)or
    (board[3]==mark and board[6]==mark and board[9]==mark)or
    (board[1]==mark and board[5]==mark and board[9]==mark)or
    (board[3]==mark and board[5]==mark and board[7]==mark))

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
def choose_first():
    if random.randint(0,1)==0:
        return 'Player1'
    else:
        return 'Player2'
    
def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    if ' ' not in board:
        return True
    else:
        return False
    
def player_choice(board,turn):
    position = 0
    acceptable_range = range(0,10)
    while position not in acceptable_range or not space_check(board,position):
        if turn=='Player1':
            position = int(input('Player-1, choose your next position (1-9) :'))
        else:
            position = int(input('Player-2, choose your next position (1-9) :'))
            
        if position not in acceptable_range:
            print('Invalid Choice!')
        elif not space_check(board,position):
            print('Position already taken!')
    return position

def replay():
    marker = 'wrong'
    while marker!='Y' and marker!='N':
        marker = input('Do you want to play again? (Y/N) :').upper()
        if marker!='Y' and marker!='N':
            print('Invalid Choice!')
    if marker=='Y':
        return True
    else:
        return False
    
def play_game():
    marker = 'wrong'
    while marker!='Y' and marker!='N':
        marker = input('Are you ready to play? (Y/N) :').upper()
        if marker!='Y' and marker!='N':
            print('Invalid Choice!')
    if marker=='Y':
        return True
    else:
        return False
    
print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' ']*10
    theBoard[0] = '#'
    player1_mark,player2_mark = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = play_game()
    
    while game_on:
        if turn == 'Player1':
            display_board(theBoard)
            position = player_choice(theBoard,turn)
            place_marker(theBoard, player1_mark, position)
            if win_check(theBoard, player1_mark):
                display_board(theBoard)
                print('Congratulations! Player-1 won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a DRAW!')
                    break
                else:
                    turn = 'Player2'
        
        else:
            display_board(theBoard)
            position = player_choice(theBoard,turn)
            place_marker(theBoard, player2_mark, position)
            if win_check(theBoard, player2_mark):
                display_board(theBoard)
                print('Congratulations! Player-2 won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a DRAW!')
                    break
                else:
                    turn = 'Player1'
            
    
    if not replay():
        break