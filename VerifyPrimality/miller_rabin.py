import random

class MillerRabin:

    @staticmethod
    def testPrimality(n: int) -> str:
        assert (n < 3 or n % 2 != 0), f"Input at MillerRabin.testPrimality(1) should be odd and greater than 3. Failed value: {n}."
        k, m = MillerRabin.__findKandM(n)
        a = random.randint(1, n-1)
        b = (a ** m) % n             

        if b % n == 1:
            return "Probably prime"
        for _ in range(0, k):    # Repeats k times.
            if (b % n == n-1):
                return "Probably prime"
            else:
                b = b**2 % n
        return "Composite"


    @staticmethod
    def __findKandM(n: int) -> tuple[int, int]:
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
