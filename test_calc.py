import unittest
from calc import sumar, resta, divide, multiplica

class TestCalcular(unittest.TestCase):
 
 def test_sumar(self):
   self.assertEqual(sumar(3, 2), 5)
   self.assertEqual(sumar(-1, 1), 0)
   self.assertEqual(sumar(-1, -1), -2)

 def test_resta(self):
   self.assertEqual(resta(5, 3),2)
   self.assertEqual(resta(5, 1),4)
   self.assertEqual(resta(2, 3),-1)

 def test_multiplica(self):
   self.assertEqual(multiplica(5, 3),15)
   self.assertEqual(multiplica(1, 3),3)
   self.assertEqual(multiplica(5, 0),0)
   
 def test_divide(self):
   self.assertEqual(divide(8, 2),4)
   self.assertEqual(divide(4, 2),2)
   self.assertEqual(divide(8, 1),8)


if __name__ == '__main__':
 unittest.main()
