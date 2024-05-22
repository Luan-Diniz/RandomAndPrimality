from random import randint
try:
    from crypto_library.VerifyPrimality.type_primality_tester import PrimalityTester
except ModuleNotFoundError:
    from type_primality_tester import PrimalityTester


class MillerRabin(PrimalityTester):

    @staticmethod
    def testPrimality(n: int, number_of_rounds: int = 1) -> str:
        assert(isinstance(n, int) and isinstance(number_of_rounds, int)
               ) ,f"Both parameters must be integers. Parameters when failed: {n}, {number_of_rounds}" 
        assert(n >= 3 and n % 2 != 0), f"Input at MillerRabin.testPrimality(1) must be odd and greater than 2. Failed value: {n}."
        assert(number_of_rounds >= 1), f"The number of rounds must be a positive integer. Failed value: {number_of_rounds}"

        for _ in range(0, number_of_rounds):
            k, m = MillerRabin.__findKandM(n)
            a = randint(1, n-1) 
            b = pow(a, m, n)   #b = (a ** m) % n    

            if b % n == 1:
                return "Probably prime"
            for _ in range(0, k):    # Iterates k times.
                if (b % n == n-1):
                    return "Probably prime"
                else:
                    b = pow(b,2,n) # b = b**2 % n
        return "Composite"


    @staticmethod
    def __findKandM(n: int) -> tuple[int, int]:     # n - 1 == 2**k * m
        k = 0
        m = 0
        n = n-1

        while True:
            if (n % 2 == 0):
                k += 1
                n /= 2
            else:
                m = n
                break
        
        return (k, int(m))
