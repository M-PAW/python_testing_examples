import unittest
from variable_conversions import varConversion

class varTests(unittest.TestCase):
    def test_toInt(self):
        self.assertEqual(varConversion.toInt("5"), 5)
        self.assertEqual(varConversion.toInt("77"),77)
        self.assertEqual(varConversion.toInt("9284"),9284)

    def test_toStr(self):
        self.assertEqual(varConversion.toStr(4),"4")
        self.assertEqual(varConversion.toStr(993),"993")
        self.assertEqual(varConversion.toStr(107),"107")

if __name__ == '__main__':
    unittest.main()