# --------Global Varibles -----------#

#Game Board
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

#If game still running
game_still_running=True

#Who won or tie?
winner=None

#varible for check the user input valid or not valid
valid_input=True

#count the number of rounds
turn =1

#Who's turn is it
current_player="X"

# display board
def display_board():
    print(board[0] +" | " + board[1]+ " | "+board[2] + " | ")
    print(board[3] +" | " + board[4]+ " | "+board[5] + " | ")
    print(board[6] +" | " + board[7]+ " | "+board[8] + " | ")
    print("                  ")

#play the game tic tac toe
def play_game():
    #display intial board
    display_board()

    # while the game is still running
    while game_still_running:

        #handle a single turn of an arbitary player
        handle_turn()

        #check if the game has ended
        check_if_game_over()

#handle a single turn of an arbitary player
def handle_turn():
    global valid_input
    global turn
    
    while valid_input:
        check_if_game_over()
        try:
            active_player = flip_flayer()
            position=input("choose a position from 1-9: ")
            position=int(position)-1

            if position > -1 and position <9:
                if board[position] == "-":
                    board[position]= active_player
                    display_board()
                    turn = turn + 1
            break
        except:
            break
        
def flip_flayer():
    
    if turn%2 == 1:
        print("X' s turn : ")
        return "X"
    else:
        print("Y's turn")
        return "O"

def check_if_game_over():
    check_for_winners()
    check_for_tie()

def check_for_winners():
    
    #setup global varibles
    global winner

    #check rows
    row_winner = check_rows()
    #check coloums
    colum_winner = check_colums()

    #check diaganols
    diagnal_winner = check_diagnals()

    if row_winner:
        winner = row_winner
    elif colum_winner:
        winner = colum_winner
    elif diagnal_winner:
        winner=diagnal_winner
    else:
        winner=None
    return


def check_rows():
    #set up Global varibles
    global game_still_running

    #check if any of the rows have all the same value  (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_running =False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return
def check_colums():
    global game_still_running

    #check if any of the rows have all the same value  (and is not empty)
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_running =False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return
def check_diagnals():
    global game_still_running

    #check if any of the rows have all the same value  (and is not empty)
    dignal_1 = board[0] == board[4] == board[8] != "-"
    diagnal_2 = board[2] == board[4] == board[6] != "-"

    if dignal_1 or diagnal_2:
        game_still_running =False
    if dignal_1:
        return board[0]
    elif diagnal_2:
        return board[2]
    return


def check_for_tie():
  # Set global variables
  global game_still_running
  # If board is full
  if "-" not in board:
    game_still_running = False
    return True
  # Else there is no tie
  else:
    return False

play_game()

#The game has ended
if winner == "X" or winner == "O":
    print(winner + " Won")
elif winner == None:
    print("Game is Tie ! Nice Play Again!")
