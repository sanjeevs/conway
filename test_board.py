import unittest
import board

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.b1 = board.Board(3,4)

  def test_out_of_bounds(self):
    self.assertTrue(self.b1.is_valid(0, 0))
    self.assertTrue(self.b1.is_valid(2, 3))
    self.assertFalse(self.b1.is_valid(3, 0))
    self.assertFalse(self.b1.is_valid(0, 4))
  
  def test_negative_bounds(self):
    self.assertTrue(self.b1.is_valid(0, 0))
    self.assertFalse(self.b1.is_valid(-1, 0))
    self.assertFalse(self.b1.is_valid(1, -1))
    self.assertFalse(self.b1.is_valid(-1, -1))

  def test_is_alive(self):
    self.assertFalse(self.b1.is_alive(0, 0))

  def test_reset(self):
    self.b1.set_alive(2,3)
    self.assertTrue(self.b1.is_alive(2, 3))
    self.b1.set_dead(2,3)
    self.assertFalse(self.b1.is_alive(2, 3))
 
  def test_neightbors_0(self):
    lst = self.b1.neighbors(0, 0)
    self.assertEqual(len(lst), 3)
    self.assertTrue((1,0) in lst)
    self.assertTrue((1,1) in lst)
    self.assertTrue((0,1) in lst)

  def test_neightbors_last(self):
    lst = self.b1.neighbors(2, 3)
    self.assertEqual(len(lst), 3)
    self.assertTrue((1,2) in lst)
    self.assertTrue((1,3) in lst)
    self.assertTrue((2,2) in lst)
  
  def test_neightbors_mid(self):
    lst = self.b1.neighbors(1, 2)
    self.assertEqual(len(lst), 8)
    self.assertTrue((0,1) in lst)
    self.assertTrue((0,2) in lst)
    self.assertTrue((0,3) in lst)
    self.assertTrue((1,3) in lst)
    self.assertTrue((2,2) in lst)
    self.assertTrue((2,3) in lst)
    self.assertTrue((1,1) in lst)
    self.assertTrue((2,1) in lst)
    self.assertTrue((2,2) in lst)
