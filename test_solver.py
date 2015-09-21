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

  def test_two_or_more_numbers_string(self):
    """Test the solver with a string of two or more numbers separated by comma"""
    cadena="1,4,9,0,4,5"
    respuesta_esperada=5
    self.assertEqual(Solver.solve(cadena),respuesta_esperada)

  def test_two_or_more_numbers_string_other_separator(self):
    """Test the solver with a string of two or more numbers separated by comma, ampersand or colon"""
    cadena = "1:6&9"
    respuesta_esperada=7
    self.assertEqual(Solver.solve(cadena),respuesta_esperada)



if __name__ == '__main__':
    unittest.main()