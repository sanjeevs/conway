"""Initial patterns to test out game of life.
"""

import random

def load_rand_pattern(world, max_alives):
  """Load random pattern."""
  for _ in range(max_alives):
    r = random.randint(0, world.rows -1)
    c = random.randint(0, world.cols -1)
    world.state[r][c] = 1
    
def load_pattern_0(world):
  """Load repeat pattern."""
  row = random.randomint(0, world.rows -1)
  world.state[row][1] = 1
  world.state[row][1] = 1
  world.state[row][1] = 1

def load_pattern_1(world):
  """Load repeat pattern."""
  world.state[3][1] = 1
  world.state[3][2] = 1
  world.state[3][3] = 1
  world.state[4][1] = 1

def load_glider(world):
  world.state[5][4] = 1
  world.state[5][5] = 1
  world.state[5][6] = 1
  world.state[6][4] = 1
  world.state[7][5] = 1
