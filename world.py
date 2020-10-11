import random

class Board:
  """This represents all the cells in the game."""

  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.state = [[0 for i in range(rows)] for j in range(cols)] 

  def set_alive(self, row, col):
    """Set the cell alive."""
    self.state[row][col] = 1

  def set_dead(self, row, col):
    """Set the cell dead."""
    self.state[row][col] = 0

  def is_alive(self, x, y):
    """Check if the position is alive."""
    return self.state[x][y]

  def is_valid_idx(self, x, y):
    """Return true if idx is within range."""
    if x < 0 or x >= self.cols:
      return False
    if y < 0 or y >= self.rows:
      return False
    return True

  def neighbors(self, x, y):
    """Return a list of neighbors to a cell.

    :param row, col position of cell
    :rtype list
    :return List of all the neighbors.
    """
    lst = []
    for i in range(-1, 2):
      for j in range(-1, 2):
        if i == 0 and j == 0:
          continue
        new_x = x + i
        new_y = y + j
        if self.is_valid_idx(new_x, new_y):
          lst.append((new_x, new_y))
    return lst

  def num_alive_neighbors(self, x, y):
    """Reurnt the number of alive neighbors."""
    alive_neighbors = [self.is_alive(x[0], x[1]) for x in self.neighbors(x, y)]
    return sum(alive_neighbors)

