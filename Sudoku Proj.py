# sudoku template
board = ([5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9])



# printing template of sudoku board
def print_board(board):
  for i_row, row in enumerate(board):
    if i_row % 3 == 0:
      print('-------------------------')
    board_row = ''
    for i_elem, elem in enumerate(row):
      if elem == 0:
        elem = ' '
      if i_elem % 3 == 0:
        board_row += '| ' + str(elem) + ' '
      elif i_elem == 8:
        board_row += str(elem) + ' |'
      else:
        board_row += str(elem) + ' '
    print(board_row)
    if i_row == 8:
      print('-------------------------')

# size of board
num_row = len(board)
num_col = len(board[0])

# find empty cell 
def find_zero(board):
  for i in range(num_row):
    for j in range(num_col):
      if board[i][j] == 0:
        return [i, j]

def is_valid(board, row, col, value):

# Row check
  if value in board[row]:
    return False

# Column check
  for i in range(len(board)):
    if board[i][col] == value:
      return False

# check for 3x3 
  r = (row - (row % 3))
  c = (col - (col % 3))
  for i in range(r, r + 3):
    for j in range(c, c + 3):
      if board[i][j] == value:
        return False  
    return True 

# solving sudoku board
def solve(board):
  zero_cell = find_zero(board)
  return solve_board_helper(board,zero_cell,1)

def solve_board_helper(board,zero_cell,value):

#base case
  if not zero_cell:
    return board
  if value > 9:
    return None

#recursion case
  if not is_valid(board,zero_cell[0],zero_cell[1],value):
    return solve_board_helper(board,zero_cell,value+1)

  board[zero_cell[0]][zero_cell[1]] = value
  solution = solve_board_helper(board,find_zero(board),1)

  if solution is not None:
    return solution

  board[zero_cell[0]][zero_cell[1]] = 0
  return solve_board_helper(board,zero_cell,value+1)