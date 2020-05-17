print("""

            TIC-TAC-TOE-GAME

            """)
board = {
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'M4': ' ', 'M5': ' ', 'M6': ' ',
    'M7': ' ', 'M8': ' ', 'M9': ' '
}

player = 1          
total_moves = 0 
end_check = 0


def check():#Checking moves of player for horizontal position
    if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
        print('Player one won !')
        return 1
    if board['M4'] == 'X' and board['M5'] == 'X' and board['M6'] == 'X':
        print('Player One Won!!')
        return 1
    if board['M7'] == 'X' and board['M8'] == 'X' and board['M9'] == 'X':
        print('Player One Won!!')
        return 1

    if board['M1'] == 'X' and board['M5'] == 'X' and board['M9'] == 'X':#Checking moves of player for DIAGONAL position
        print('Player One Won!!')
        return 1
    if board['M1'] == 'X' and board['M4'] == 'X' and board['M7'] == 'X':#Checking moves of player for VERTICAL position
        print('Player One Won!!')
        return 1
    if board['M2'] == 'X' and board['M5'] == 'X' and board['M8'] == 'X':
        print('Player One Won!!')
        return 1
    if board['M3'] == 'X' and board['M6'] == 'X' and board['M9'] == 'X':
        print('Player One Won!!')
        return 1
    if board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':#NOW PAYER2 
        print('Player Two Won!!')
        return 1 
    if board['M4'] == 'O' and board['M5'] == 'O' and board['M6'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['M7'] == 'O' and board['M8'] == 'O' and board['M9'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['M1'] == 'O' and board['M5'] == 'O' and board['M9'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['M1'] == 'O' and board['M4'] == 'O' and board['M7'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['M2'] == 'O' and board['M5'] == 'O' and board['M8'] == 'O':
        print('Player Two Won!!')
        return 1
    if board['M3'] == 'O' and board['M6'] == 'O' and board['M9'] == 'O':
        print('Player Two Won!!')
        return 1
    return 0

print('-- +--+--')
print('|M1|M2|M3|')
print('-- +--+--')
print('|M4|M5|M6|')
print('-- +--+--')
print('|M7|M8|M9|')
print('-- +--+--')

print('-x-o-x-o-x-o-GAME START-o-x-o-x-o-x-')

while True:
    print('--+-+--')
    print('|'       +   board['M1'] +           '|'         +   board['M2'] +       '|'+    board['M3'] +        '|')
    print('--+-+--')   
    print('|'       +   board['M4'] +           '|'         +   board['M5'] +       '|'+    board['M6'] +        '|')
    print('--+-+--')
    print('|'       +   board['M7'] +           '|'         +   board['M8'] +       '|'+    board['M9'] +        '|')
    print('--+-+--')
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:     # input from players
        if player == 1:  # choose player
            p1_input = input('player1 your turn: ')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            # on wrong input
            else:
                print('Invalid input, please try again')
                continue
        else:
            p2_input = input('player2 your turn: ')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            else:  # on wrong input
                print('Invalid input, please try again')
                continue
    total_moves += 1
print('-x-o-x-o-x-o-GAME OVER-o-x-o-x-o-x-')
print()
input('\n\n press ENTER to exit\n')

