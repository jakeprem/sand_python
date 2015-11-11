import unittest
import fibo

class TestFiboMethods(unittest.TestCase):

  def test_fib(self):
      self.assertEqual(fibo.fib(1000), 'FOO')

  def test_fib2(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()