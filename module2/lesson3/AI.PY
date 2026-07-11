import random
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
    print(' ' + colored(board[0]) + ' | ' + colored(board[1]) + ' | ' + colored(board[2]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[3]) + ' | ' + colored(board[4]) + ' | ' + colored(board[5]))
    print(Fore.CYAN + '-----------' + Style.RESET_ALL)
    print(' ' + colored(board[6]) + ' | ' + colored(board[7]) + ' | ' + colored(board[8]))
    print()

def player_choice():
    symbol = ''
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
    if symbol == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def player_move(board, symbol):
    user_input = -1
    while user_input not in range(1,10) or not board[user_input-1].isdigit():
        try:
            user_input = int(input("Enter a number between 1-9: "))
            if user_input not in range(1,10) or not board[user_input-1].isdigit():
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter a valid number.")
    board[user_input-1] = symbol

def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol

def check_win(board, symbol):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == symbol for i in condition):
            return True
    return False

def check_full(board):
    return all(not cell.isdigit() for cell in board)

def tic_tac_toe():
    print(Fore.GREEN + "Welcome to Tic-Tac-Toe!" + Style.RESET_ALL)
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)

    while True:
        board = [str(i+1) for i in range(9)]
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            display_board(board)
            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"Congratulations {player_name}, you win!" + Style.RESET_ALL)
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
                    game_on = False
                else:
                    turn = 'AI'
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "AI wins! Better luck next time." + Style.RESET_ALL)
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a tie!" + Style.RESET_ALL)
                    game_on = False
                else:
                    turn = 'Player'

        play_again = input(Fore.GREEN + "Do you want to play again? (yes/no): " + Style.RESET_ALL).lower()
        if play_again != 'yes':
            print(Fore.CYAN + f"Thanks for playing, {player_name}!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    tic_tac_toe()
