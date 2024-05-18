import unittest, pprint
from miller_rabin import MillerRabin

class TestMillerRabin(unittest.TestCase):

    def test_prime_number(self):
        primes = [3, 7, 11, 19, 1447, 2909, 3187, 4421, 5693, 6833, 7639, 7919]
        for number in primes:
            self.assertEqual("Probably prime", MillerRabin.testPrimality(number),
                              f"Miller Rabin failed the test with value {number}.")

    def test_carmichael_numbers(self):
        iterations = 1000
        carmichael_numbers = { 561: 0, 1105: 0, 1729 : 0, 2465 : 0, 2821 : 0,
                                6601 : 0, 8911 : 0 }
        
        for number in carmichael_numbers:
            for _ in range(0,iterations):
                if MillerRabin.testPrimality(number) == "Probably prime":
                    carmichael_numbers[number] += 1
        print()
        print("Carmichael number : times it passed the Miller-Rabin test.")
        pprint.PrettyPrinter(width = 40, depth= 2).pprint(carmichael_numbers)
        print()

    def test_wrong_parameters(self):
        with self.assertRaises(AssertionError):
            MillerRabin.testPrimality(1)    # n < 3
        with self.assertRaises(AssertionError):
            MillerRabin.testPrimality(222)  # n even
        with self.assertRaises(TypeError):
            MillerRabin.testPrimality("gremio") # n not being a number
            

if __name__ == '__main__':
    unittest.main()
