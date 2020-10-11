import unittest
import world 
import rules

class TestRules(unittest.TestCase):
  def setUp(self):
    self.b1 = world.World(4,4)

  def test_rule_born(self):
    self.b1.set_alive(1,1)
    self.b1.set_alive(2,1)
    self.b1.set_alive(2,2)
    self.assertEqual(self.b1.num_alive_neighbors(1,1), 2)
    self.assertEqual(self.b1.num_alive_neighbors(2,1), 2)
    self.assertEqual(self.b1.num_alive_neighbors(2,2), 2)
    self.assertEqual(self.b1.num_alive_neighbors(1,2), 3)
    self.assertEqual(rules.get_next_cell_state(self.b1, 1, 2), 1)
    self.assertEqual(rules.get_next_cell_state(self.b1, 1, 1), 1)
    self.assertEqual(rules.get_next_cell_state(self.b1, 2, 1), 1)
    self.assertEqual(rules.get_next_cell_state(self.b1, 2, 2), 1)
    
  def test_rule_dead(self):
    self.b1.set_alive(1,1)
    self.b1.set_alive(1,2)
    self.b1.set_alive(2,1)
    self.b1.set_alive(2,2)
    self.assertEqual(self.b1.num_alive_neighbors(0,0), 1)
    self.assertEqual(self.b1.num_alive_neighbors(0,1), 2)
    self.assertEqual(self.b1.num_alive_neighbors(0,2), 2)
    self.assertEqual(self.b1.num_alive_neighbors(0,3), 1)
    self.assertEqual(rules.get_next_cell_state(self.b1, 0, 0), 0)
    self.assertEqual(rules.get_next_cell_state(self.b1, 0, 1), 0)
    self.assertEqual(rules.get_next_cell_state(self.b1, 0, 2), 0)
    self.assertEqual(rules.get_next_cell_state(self.b1, 0, 3), 0)
    self.assertEqual(self.b1.num_alive_neighbors(0,3), 1)
    self.assertEqual(self.b1.num_alive_neighbors(1,3), 2)
    self.assertEqual(self.b1.num_alive_neighbors(2,3), 2)
    self.assertEqual(self.b1.num_alive_neighbors(3,3), 1)

  def test_rule_living(self):
    self.b1.set_alive(0, 1)
    self.b1.set_alive(1, 0)
    self.b1.set_alive(1, 2)
    self.b1.set_alive(2, 1)
    self.b1.set_alive(2, 2)
    self.assertEqual(rules.get_next_cell_state(self.b1, 0, 0), 0)
    self.assertEqual(rules.get_next_cell_state(self.b1, 0, 1), 1)
    self.assertEqual(rules.get_next_cell_state(self.b1, 1, 0), 1)
    self.assertEqual(rules.get_next_cell_state(self.b1, 1, 2), 1)
    self.assertEqual(rules.get_next_cell_state(self.b1, 2, 1), 1)
    self.assertEqual(rules.get_next_cell_state(self.b1, 2, 2), 1)

  def test_rule_dying(self):
    self.b1.set_alive(0, 0)
    self.b1.set_alive(0, 1)
    self.b1.set_alive(0, 2)
    self.b1.set_alive(1, 1)
    self.b1.set_alive(2, 0)
    self.b1.set_alive(2, 1)
    self.b1.set_alive(2, 2)
    self.b1.set_alive(3, 3)
    self.assertEqual(rules.get_next_cell_state(self.b1, 1, 1), 0)
    self.assertEqual(rules.get_next_cell_state(self.b1, 3, 3), 0)
    self.assertEqual(rules.get_next_cell_state(self.b1, 2, 0), 1)

