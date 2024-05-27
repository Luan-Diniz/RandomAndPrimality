import unittest, pprint
from miller_rabin import MillerRabin


class TestMillerRabin(unittest.TestCase):

    def test_prime_number(self):
        primes = [5, 7, 11, 19, 1447, 2909, 3187, 4421, 5693, 6833, 7639, 7919]
        for number in primes:
            self.assertEqual("Probably prime", MillerRabin.testPrimality(number),
                              f"Miller Rabin failed the test with value {number}.")

    def test_carmichael_numbers(self):
        iterations = 1000
        carmichael_numbers = {
            561: 0 ,
            1105: 0,
            2465: 0,
            6601: 0,
            8911: 0,
            10585: 0,
            11972017: 0,
            67902031: 0,
            1208361237478669: 0, 
            844154128953833755776750022681: 0 ,
            365376903642671522645639268043801: 0 ,
            392000251605356793349050844538065236557716721692385776886401: 0,
            2706440581932960270059556320865135299543027488341564061948937275059222956610372230689798686533299112388959963299201: 0
        }
        
        for number in carmichael_numbers:
            for _ in range(0,iterations):
                if MillerRabin.testPrimality(number) == "Probably prime":
                    carmichael_numbers[number] += 1
        print()
        print("Carmichael number : times it passed the Miller-Rabin test.")
        pprint.PrettyPrinter(width = 40, depth= 2).pprint(carmichael_numbers)
        print()

    def test_wrong_parameters(self):
        test_cases = [
            (1, AssertionError),             # n < 3
            (222, AssertionError),           # n even
            (19, 0, AssertionError),         # number_of_rounds < 1
            (19, 2.5, AssertionError),       # number_of_rounds not an integer
            (19.5, 3, AssertionError),       # n not an integer
            ("gremio", AssertionError),      # n not being a number
            (19, "gremio", AssertionError)   # number_of_rounds not being a number
        ]

        for *parameters, error in test_cases:
            with self.assertRaises(error):
                MillerRabin.testPrimality(*parameters)
                

if __name__ == '__main__':
    unittest.main()
