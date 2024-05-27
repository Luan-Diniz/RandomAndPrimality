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
   
        fermat_pseudoprimes = {
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
        
        


        for number in fermat_pseudoprimes:
            for _ in range(0,iterations):
                if FermatPrimalityTest.testPrimality(number, 1) == "Probably prime":
                    fermat_pseudoprimes[number] += 1
        print()
        print("Fermat Pseudoprimes : times it passed the Fermat Primality Test test.")
        pprint.PrettyPrinter(width = 40, depth= 2).pprint(fermat_pseudoprimes)
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
