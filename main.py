
from utils import *
from random import randint

if __name__ == '__main__':
    #sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    sizes = [80]

    #TODO: 
    # Measure of execution time to create the random numbers and test its primality.
         
    for size in sizes:
        lcg = LinearCongruentialGenerator(randint(0, 1000000) ,2**32,1664525,1013904223)   # m = 2**32, a = 1664525, c = 1013904223 From Wikipedia
        number = RandomNumberWithSpecificSize(size, 32, lcg)
        print(number)
        print("PRIME: ", end = "")
        print(FindPrimeNumberWithSpecificSize(size, number, MillerRabin.testPrimality))
        print()