condition = True
while condition:

    print('paper - I, scissors - X, rock - O')
    player1 = raw_input("first player desision: ")
    player2 = raw_input("first player desision: ")

    if player1 == player2:
        print('one more time')
        continue
    if player1 == 'I':
        if player2 == 'X':
            print("Player 2 won!")
        if player2 == 'O':
            print("player 1 won!")
    if player1 == 'X':
        if player2 == 'O':
            print("Player 2 won!")
        if player2 == 'I':
            print("player 1 won!")
    if player1 == 'O':
        if player2 == 'I':
            print("Player 2 won!")
        if player2 == 'X':
            print("player 1 won!")

    decision = raw_input('Again? Yes/No: ')
    if decision == 'Yes':
        condition = True
    else:
        condition = False
