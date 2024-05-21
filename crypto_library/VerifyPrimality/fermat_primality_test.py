from random import randint
try:
    from crypto_library.VerifyPrimality.type_primality_tester import PrimalityTester
except ModuleNotFoundError:
    from type_primality_tester import PrimalityTester


class FermatPrimalityTest(PrimalityTester):

    @staticmethod
    def testPrimality(n: int, number_of_rounds: int = 1) -> str:
        assert(isinstance(n, int) and isinstance(number_of_rounds, int)
               ), f"Both parameters must be integers. Parameters when failed: {n}, {number_of_rounds}" 
        assert(n > 3), f"Input at FermatPrimalityTest.testPrimality(1) must be greater than 3. Failed value: {n}."
        assert(number_of_rounds >= 1), f"The number of rounds must be a positive integer. Failed value: {number_of_rounds}"

        # Would be possible to an even number pass the Fermat Primality Test without the line below.
        if (n % 2 == 0):            
            return "Composite"

        for _ in range(0, number_of_rounds):   
            a = randint(2, n-2)
            if (a**(n-1) % n != 1):
                return "Composite"
        return "Probably prime"