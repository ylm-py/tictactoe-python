# Created by : Yassine Lemrani


# board of the game with key and value set to empty string
board = {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
total_moves = 0
player = 1
while True:
    # Checking if one of the players won and returning True and storing it in 'x'
    def horizontal_check(x):
        if board[1] == 'X' and board[2] == 'X' and board[3] == 'X':
            print('Player 1 Won !')
            return True
        if board[4] == 'X' and board[5] == 'X' and board[6] == 'X':
            print('Player 1 Won !')
            return True
        if board[7] == 'X' and board[8] == 'X' and board[9] == 'X':
            print('Player 1 Won !')
            return True

        if board[1] == 'O' and board[2] == 'O' and board[3] == 'O':
            print('Player 2 Won !')
            return True
        if board[4] == 'O' and board[5] == 'O' and board[6] == 'O':
            print('Player 2 Won !')
            return True
        if board[7] == 'O' and board[8] == 'O' and board[9] == 'O':
            print('Player 2 Won !')
            return True


    def vertical_check(x):
        if board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
            print('Player 1 Won !')
            return True
        if board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
            print('Player 1 Won !')
            return True
        if board[3] == 'X' and board[6] == 'X' and board[9] == 'X':
            print('Player 1 Won !')
            return True

        if board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
            print('Player 2 Won !')
            return True
        if board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
            print('Player 2 Won !')
            return True
        if board[3] == 'O' and board[6] == 'O' and board[9] == 'O':
            print('Player 2 Won !')
            return True


    def diagonal_check(x):
        if board[1] == 'X' and board[5] == 'X' and board[9] == 'X':
            print('Player 1 Won !')
            return True
        if board[3] == 'X' and board[5] == 'X' and board[7] == 'X':
            print('Player 1 Won !')
            return True
        
        if board[1] == 'O' and board[5] == 'O' and board[9] == 'O':
            print('Player 2 Won !')
            return True
        if board[3] == 'O' and board[5] == 'O' and board[7] == 'O':
            print('Player 2 Won !')
            return True


    print('''
        1 | 2 | 3
        ----------
        4 | 5 | 6
        ----------
        7 | 8 | 9
    ''')
    print(board[1] + '    |    ' + board[2] + '    |    ' + board[3])
    print('------------------')
    print(board[4] + '    |    ' + board[5] + '    |    ' + board[6])
    print('------------------')
    print(board[7] + '    |    ' + board[8] + '    |    ' + board[9])

    # for every time the loop starts again we need to check if someone won or if the total moves is equal to 9

    if vertical_check(True) or horizontal_check(True) or diagonal_check(True):
        break
    if total_moves == 9:
        print('Draw\n')
        break




    if player == 1:
        # Using this while loop to force the user to enter a valid input which should be a number and if not they get a friendly error message
        while True:
            try:
                user_command = int(input('Player 1 (X) : '))
                break
            except ValueError:
                print('Please enter a valid number')
        # Checking if the case choosed by the user is empty
        if user_command in board and board[user_command] == '':
            board[user_command] = 'X'
            total_moves += 1
            player = 2
        if board[user_command] != '':
            print('Already Full , Choose an empty case !')
    elif player == 2:
        while True:
            try:
                user_command = int(input('Player 2 (O) : '))
                break
            except ValueError:
                print('Please enter a valid number')
        if user_command in board and board[user_command] == '':
            board[user_command] = 'O'
            total_moves += 1
            player = 1
        if board[user_command] != '':
            print('Already Full , Choose an empty case !')




