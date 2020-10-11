import board
import rules
import gui
import random
import time
from patterns import *

def main(nrows, ncols, nticks, max_alives):
  px_width = 2 
  display = gui.Gui(nrows, ncols, px_width)

  boards = [board.Board(nrows, ncols), board.Board(nrows, ncols)]
  curr_idx = 0
  load_rand_pattern(boards[curr_idx], 500)
  display.update(boards[curr_idx])
  input("Press any key to start to the game.")

  for t in range(nticks):
    nxt_idx = (curr_idx + 1) % 2

    for i in range(nrows):
      for j in range(ncols):
        if rules.get_next_cell_state(boards[curr_idx], i, j) == 1:
          boards[nxt_idx].set_alive(i, j)
        else:
          boards[nxt_idx].set_dead(i, j)
  
    display.update(boards[nxt_idx])
    curr_idx = nxt_idx
    time.sleep(1)

if __name__ == "__main__":
  print("Running Conway Game Of Life")
  main(512, 512, 1000, 100)


