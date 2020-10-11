"""Initial patterns to test out game of life.
  It assumes a 8x8 board.state space.
"""
import random

def load_rand_pattern(board, max_alives):
  """Load random pattern."""
  for _ in range(max_alives):
    r = random.randint(0, board.rows -1)
    c = random.randint(0, board.cols -1)
    board.state[r][c] = 1
    
def load_pattern_0(board):
  """Load repeat pattern."""
  row = random.randomint(0, board.rows -1)
  board.state[row][1] = 1
  board.state[row][1] = 1
  board.state[row][1] = 1

def load_pattern_1(board):
  """Load repeat pattern."""
  board.state[3][1] = 1
  board.state[3][2] = 1
  board.state[3][3] = 1
  board.state[4][1] = 1

def load_glider(board):
  board.state[5][4] = 1
  board.state[5][5] = 1
  board.state[5][6] = 1
  board.state[6][4] = 1
  board.state[7][5] = 1
