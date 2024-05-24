import unittest, pprint
from random import randint
from fermat_primality_test import FermatPrimalityTest


class TestFermatPrimalityTest(unittest.TestCase):

    def test_prime_number(self):
        primes = [7, 11, 19, 1447, 2909, 3187, 4421, 5693, 6833, 7639, 7919]
        for number in primes:
            self.assertEqual("Probably prime", FermatPrimalityTest.testPrimality(number),
                                f"Fermat Primality Test failed the test with value {number}.")

    def test_even_number(self):
        iterations = 100
        for _ in range(0, iterations):
            even_number = randint(3, 1000) * 2
            self.assertEqual("Composite", FermatPrimalityTest.testPrimality(even_number),
                              f"Fermat Primality Tested failed with value {even_number}.")

    def test_fermat_pseudoprimes(self):
        iterations = 1000
        carmichael_numbers = { 561: 0, 1105: 0, 1729 : 0, 2465 : 0, 2821 : 0,
                                6601 : 0, 8911 : 0, 341: 0, 645: 0, 1387: 0, 1905: 0 }
        
        for number in carmichael_numbers:
            for _ in range(0,iterations):
                if FermatPrimalityTest.testPrimality(number) == "Probably prime":
                    carmichael_numbers[number] += 1
        print()
        print("Fermat Pseudoprimes : times it passed the Fermat Primality Test test.")
        pprint.PrettyPrinter(width = 40, depth= 2).pprint(carmichael_numbers)
        print()

    def test_wrong_parameters(self):
        test_cases = [
            (3, AssertionError),             # n <= 3
            (19, 0, AssertionError),         # number_of_rounds < 1
            (19, 2.5, AssertionError),       # number_of_rounds not an integer
            (19.5, 3, AssertionError),       # n not an integer
            ("gremio", AssertionError),      # n not being a number
            (19, "gremio", AssertionError)   # number_of_rounds not being a number
        ]

        for *parameters, error in test_cases:
            with self.assertRaises(error):
                FermatPrimalityTest.testPrimality(*parameters)
            

if __name__ == '__main__':
    unittest.main()
