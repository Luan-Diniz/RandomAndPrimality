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
        assert(n > 3 and n % 2 != 0), f"Input at MillerRabin.testPrimality(1) must be odd and greater than 2. Failed value: {n}."
        assert(number_of_rounds >= 1), f"The number of rounds must be a positive integer. Failed value: {number_of_rounds}"


        s, d = MillerRabin.__findSandD(n)

        for _ in range(0, number_of_rounds):
            a = randint(2, n-2)
            x = pow(a,d,n)
            for _ in range(0, s):
                y = (x ** 2) % n
                if y == 1 and x != 1 and x != n-1:
                    return "Composite"
                x = y
            if y != 1:
                return "Composite"
        return "Probably prime"
    
    @staticmethod
    def __findSandD(n: int) -> tuple[int, int]:     # n - 1 == 2**s * d
        s = 0
        d = 0
        n = n-1

        while True:
            if (n % 2 == 0):
                s += 1
                n = n // 2
            else:
                d = n
                break
        
        return (s, d)
