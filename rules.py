"""This encodes conway game of life rules."""

def get_next_cell_state(board, row, col):
  """Return the next state of the cell.

    :param board: board representing the state of all the cells.
    :param row, col: row, col position of cell. 
  """

  num_alive_neighbors = board.num_alive_neighbors(row, col)
  if not board.is_alive(row, col):
    if num_alive_neighbors == 3:
      return 1
    else:
      return 0
  else:
    if num_alive_neighbors == 2 or num_alive_neighbors == 3:
      return 1
    else:
      return 0

  
