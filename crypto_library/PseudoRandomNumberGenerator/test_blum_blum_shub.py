import unittest
from blum_blum_shub import BlumBlumShub


class TestBlumBlumShub(unittest.TestCase):
    def test_number_generation(self):
        result = []
        bbs = BlumBlumShub(5, 7, 11)  # Xo = 5 , p = 7, q = 11
        for _ in range(0,4):
            result.append(bbs.generateNumber())
        self.assertEqual([25, 9, 4, 16], result, f"generateNumber(0) failed the test.")

        result = [
            bbs.getXiValue(0), bbs.getXiValue(1),
            bbs.getXiValue(2), bbs.getXiValue(3),
            bbs.getXiValue(4)
        ]
        self.assertEqual([5, 25, 9, 4, 16], result, f"getXivalue(1) failed the test.")

    def test_iterator(self):
        result = []
        bbs = BlumBlumShub(2198404, 4783, 6199)   # Xo = 2198404, p = 4783, q = 6199
        for number in bbs.generateGenerator(5):
            result.append(number)

        self.assertEqual([676582, 29327878, 18609306, 24519310, 2638227], result,
                          f"Iterator failed the test.")


    def test_wrong_parameters(self):
        test_cases = [
            (1.5, 1, 1, AssertionError),          
            ("gremio", 1, 1, AssertionError),      
        ]

        for *parameters, error in test_cases:
            with self.assertRaises(error):
                BlumBlumShub(*parameters)


if __name__ == '__main__':
    unittest.main()
