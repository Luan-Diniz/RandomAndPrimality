from PseudoRandomNumberGenerator import *
from VerifyPrimality import *

if __name__ == '__main__':
    '''
    print("Hello World")   # Run tests.

    lcg = LinearCongruentialGenerator(3,9,7,4)  #Xo = 3, m = 9, a = 7 , c = 4
    for i in lcg.generateGenerator(9):      # Exemplo do slide
        print(i)
    '''

    #Note: Carmichael numbers can fail the test. Probabilistic, the algorithm can say sometimes that 561 is Probably Prime instead of Composite
    print(MillerRabin.testPrimality(561))  # 561 is not a prime (composite)
    print(MillerRabin.testPrimality(1105)) # 1105 is not prime (composite)
    print(MillerRabin.testPrimality(613))  # 613 is prime
    print(MillerRabin.testPrimality(2047)) # 2047 is composite (already failed a test)
    
    composite_passed_MilleRabin_count = 0
    for i in range(0,1000):
        if (MillerRabin.testPrimality(561) == "Probably prime"):
            composite_passed_MilleRabin_count += 1
    print(composite_passed_MilleRabin_count)


    # See https://docs.python.org/3/library/unittest.html for creating and running theses tests easily.