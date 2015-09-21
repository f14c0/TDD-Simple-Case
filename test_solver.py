import unittest
import Solver
__author__ = 'JULIAN'


class TestSolver(unittest.TestCase):

  def test_solve_empty_string(self):
    """Test if  empty string returns 0"""
    self.assertEqual(Solver.solve(""),0)

  def test_one_number_string(self):
    """Tesf if string wiht one number returns its number"""
    cadena = "1"
    self.assertEqual(Solver.solve(cadena),cadena)





if __name__ == '__main__':
    unittest.main()