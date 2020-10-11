"""Conwacol world with all the cells."""

class World:
  """This represents all the cells in the game."""

  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.state = [[0 for i in range(cols)] for j in range(rows)] 

  def set_alive(self, row, col):
    """Set the cell alive."""
    self.state[row][col] = 1

  def set_dead(self, row, col):
    """Set the cell dead."""
    self.state[row][col] = 0

  def is_alive(self, row, col):
    """Check if the position is alive."""
    return self.state[row][col]

  def is_valid_idx(self, row, col):
    """Return true if idx is within range."""
    if row < 0 or row >= self.rows:
      return False
    if col < 0 or col >= self.cols:
      return False
    return True

  def neighbors(self, row, col):
    """Return a list of neighbors to a cell.

    :param row, col position of cell
    :rtcolpe list
    :return List of all the neighbors.
    """
    lst = []
    for i in range(-1, 2):
      for j in range(-1, 2):
        if i == 0 and j == 0:
          continue
        new_row = row + i
        new_col = col + j
        if self.is_valid_idx(new_row, new_col):
          lst.append((new_row, new_col))
    return lst

  def num_alive_neighbors(self, row, col):
    """Reurnt the number of alive neighbors."""
    alive_neighbors = [self.is_alive(row[0], row[1]) for row in self.neighbors(row, col)]
    return sum(alive_neighbors)

  def __eq__(self, other):
    return self.state == other.state  
