import unittest
from variable_conversions import varConversion

class varTests(unittest.TestCase):
    def test_toInt(self):
        self.assertEqual(varConversion.toInt("5"), 5)

if __name__ == '__main__':
    unittest.main()