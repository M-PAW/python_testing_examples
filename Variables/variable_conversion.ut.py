import unittest
from variable_conversions import varConversion

class varTests(unittest.TestCase):
    # def test_toInt(self):
    #     self.assertEqual(varConversion.toInt("5"), 5)
    #     self.assertEqual(varConversion.toInt("77"),77)
    #     self.assertEqual(varConversion.toInt("9284"),9284)

    # def test_toStr(self):
    #     self.assertEqual(varConversion.toStr(4),"4")
    #     self.assertEqual(varConversion.toStr(993),"993")
    #     self.assertEqual(varConversion.toStr(107),"107")

    # def test_arrToInt(self):
    #     self.assertEqual(varConversion.arrToInt(['1','3','5','7','0']),[2,6,10,14,0])
    #     self.assertEqual(varConversion.arrToInt(['8','5','7','2','6']),[16,10,14,4,12])
    #     self.assertEqual(varConversion.arrToInt(['7','4','0','4','1']),[14,8,0,8,2])

    def test_thirdElement(self):
        self.assertEqual(varConversion.thirdElement(['This','That','What','Where','How']),['This','That','Where','How'])
        self.assertEqual(varConversion.thirdElement(['Why','What','Where','How','Who']),['Why','What','How','Who'])
        self.assertEqual(varConversion.thirdElement(['What','How','Who','Where','Why']),['What','How','Where','Why'])

if __name__ == '__main__':
    unittest.main()