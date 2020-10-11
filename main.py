import world 
import rules
import gui
import random
import time
from patterns import *

def main(nrows, ncols, px_width):
  display = gui.Gui(nrows, ncols, px_width)

  worlds = [world.World(nrows, ncols), world.World(nrows, ncols)]
  curr_world = worlds[0]
  nxt_world = worlds[1]
  max_alives = int((nrows * ncols) / 5)
  load_rand_pattern(curr_world, max_alives)
  #load_glider(curr_world)
  display.update(curr_world)

  nticks = 0
  while 1:
    run_tick(curr_world, nxt_world)
    if curr_world == nxt_world:
      print("World is dead!!")
      break
    display.update(nxt_world)
    curr_world, nxt_world = nxt_world, curr_world
    time.sleep(0.1)
    nticks += 1
    if nticks % 100 == 0:
      print("++Finished Tick=", nticks)

  print(">>Ran the sim for ticks=" + str(nticks))

def run_tick(world, nxt_world):
  """Run a single tick and update the new world."""
  for i in range(world.rows):
    for j in range(world.cols):
        if rules.get_next_cell_state(world, i, j) == 1:
          nxt_world.set_alive(i, j)
        else:
          nxt_world.set_dead(i, j)


if __name__ == "__main__":
  print("Running Conway Game Of Life")
  main(nrows=100, ncols=100, px_width=5)


