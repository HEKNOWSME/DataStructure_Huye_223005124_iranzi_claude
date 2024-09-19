board = [
     ["x", "o", "x"], # row 1
     ["o", "x", "o"], # row 2
     ["o", "x", "o"], # row 3
]
def check_winner(board): 
     for row in board:
          if row[0] == row[1] == row[2] != "":
               return f"the winner is {row[0]}"
     for col in range(3):
          if board[0][col] == board[1][col] == board[2][col] != "":
               return f"the winner is {board[0][col]}"
     if board[0][0] == board[1][1] == board[2][2] != "":
          return f"the winner is {board[0][0]}"
     return "Toe"
print(check_winner(board))