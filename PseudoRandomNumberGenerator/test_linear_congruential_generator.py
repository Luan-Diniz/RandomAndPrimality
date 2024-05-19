import unittest
from linear_congruential_generator import LinearCongruentialGenerator

class TestLinearCongruentialGenerator(unittest.TestCase):

    def test_number_generation(self):
        result = []
        lcg = LinearCongruentialGenerator(1,9,2,0)  #Xo = 1, m = 9, a = 2 , c = 0
        for _ in range(0, 6):   # Generates six numbers.
            result.append(lcg.generateNumber())
        self.assertEqual([2,4,8,7,5,1], result, f"Failed the test.")

    def test_iterator(self):
        result = []
        lcg = LinearCongruentialGenerator(3,9,7,4)  #Xo = 3, m = 9, a = 7 , c = 4
        for number in lcg.generateGenerator(12):
            result.append(number)
        self.assertEqual([7,8,6,1,2,0,4,5,3,7,8,6], result, f"Failed the test.")

    def test_wrong_parameters(self):
        test_cases = [
            (1.5, 1, 1, 1, AssertionError),          
            ("gremio", 1, 1, 1, AssertionError),      
        ]

        for *parameters, error in test_cases:
            with self.assertRaises(error):
                LinearCongruentialGenerator(*parameters)


if __name__ == '__main__':
    unittest.main()
