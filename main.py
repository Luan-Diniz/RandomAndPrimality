from utils import *
from random import randint
from time import time


if __name__ == '__main__':
    sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    
    """
    #######################################################################################
    # Measuring the time for generating one number of each size.

    start_time_all_randons = time()
    for size in sizes:
        print("Linear Congruential Generator")
        print(f"Size: {size} bits")
        start_time = time()
        lcg = LinearCongruentialGenerator(randint(0, 1000000) ,2**32,1664525,1013904223)   # m = 2**32, a = 1664525, c = 1013904223 From Wikipedia
        number = RandomNumberWithSpecificSize(size, 32, lcg)
        end_time =time()
        print(f"Execution time: {end_time - start_time}s")
        print(f"Number generated: {number}")
        print()
    end_time_all_randons = time()
    print(f"Total Time Linear Congruential Generator: {end_time_all_randons - start_time_all_randons}s")
    print("-------------------------------------------------------------")
    print()

    start_time_all_randons = time()
    for size in sizes:
        print("Blum Blum Shub")
        print(f"Size: {size} bits")
        start_time = time()
        bbs = BlumBlumShub(randint(0, 1000000), 3263052707, 5847777359)   # p = 3263052707, q = 5847777359
        number = RandomNumberWithSpecificSize(size, 64, bbs)
        end_time = time()
        print(f"Execution time:  {(end_time - start_time)}s")
        print(f"Number generated: {number}")
        print()
    end_time_all_randons = time()
    print(f"Total Time BlumBlumShub: {end_time_all_randons - start_time_all_randons}s")
    print("-------------------------------------------------------------")
    print()


    #######################################################################################
    # Measuring the time for generating many numbers of a specific size.
    size = 4096
    number_iterations = 10000

    print(f"Generating {number_iterations} numbers of {size} bits...")
    start_time_all_randons = time()
    for _ in range(0, number_iterations):
        lcg = LinearCongruentialGenerator(randint(0, 1000000) ,2**32,1664525,1013904223)   # m = 2**32, a = 1664525, c = 1013904223 From Wikipedia
        number = RandomNumberWithSpecificSize(size, 32, lcg)
    end_time_all_randons = time()
    print(f"Total Time Linear Congruential Generator: {end_time_all_randons - start_time_all_randons}s")
    print("-------------------------------------------------------------")
    print()

    print(f"Generating {number_iterations} numbers of {size} bits...")
    start_time_all_randons = time()
    for _ in range(0, number_iterations):
        bbs = BlumBlumShub(randint(0, 1000000), 3263052707, 5847777359)   # p = 3263052707, q = 5847777359
        number = RandomNumberWithSpecificSize(size, 64, bbs)
    end_time_all_randons = time()
    print(f"Total Time Blum Blum Shub Generator: {end_time_all_randons - start_time_all_randons}s")
    print("-------------------------------------------------------------")
    print()


    #######################################################################################
    # Measuring the time for generating a prime number of each size.
    # Note: The generation time of a random number has little impact on the total execution time. 
    # That's why it is tested here only with Linear Congruential Generator. 

    start_time_all_primes = time()
    for size in sizes:
        print("Fermat Primality Test")
        print(f"Size: {size} bits")
        start_time = time()
        prime_number = FindPrimeNumberWithSpecificSize(size, FermatPrimalityTest.testPrimality, 32, lcg)
        end_time = time()
        print(f"Execution time:  {(end_time - start_time)}s")
        print(f"Number generated: {prime_number}")
        print()
    end_time_all_primes = time()
    print(f"Total Time Fermat Primality Test: {end_time_all_primes - start_time_all_primes}s")
    print("-------------------------------------------------------------")
    print()

    start_time_all_primes = time()
    for size in sizes:
        print("Miller-Rabin")
        print(f"Size: {size} bits")
        start_time = time()
        prime_number = FindPrimeNumberWithSpecificSize(size, MillerRabin.testPrimality, 32, lcg)
        end_time = time()
        print(f"Execution time:  {(end_time - start_time)}s")
        print(f"Number generated: {prime_number}")
        print()
    end_time_all_primes = time()
    print(f"Total Time Miller-Rabin: {end_time_all_primes - start_time_all_primes}s")
    print("-------------------------------------------------------------")
    print()
    """
    lcg = LinearCongruentialGenerator(randint(0, 1000000) ,2**32,1664525,1013904223)  #DELETE THIS LINE
    #######################################################################################
    # Measuring the average time for generating a prime number of specific size.
    # Note: The generation time of a random number has little impact on the total execution time. 
    # That's why it is tested here only with Linear Congruential Generator. 
    sizes = [1024, 2048, 4096]
    number_iterations = 25

    for size in sizes:
        iterations_time = []
        start_time_all_primes = time()
        print(f"Generating {number_iterations} prime numbers of {size} bits...")
        print("Fermat Primality Test")
        for _ in range(0, number_iterations):
            start_time = time()
            prime_number = FindPrimeNumberWithSpecificSize(size, FermatPrimalityTest.testPrimality, 32, lcg)
            end_time = time()
            iterations_time.append(end_time - start_time)
            

        end_time_all_primes = time()
        print(f"Average Time Fermat Primality Test: {(end_time_all_primes - start_time_all_primes)/number_iterations}s")
        print(f"All measured times: {iterations_time}")
        print("-------------------------------------------------------------")
        print()


        iterations_time = []
        start_time_all_primes = time()
        print(f"Generating {number_iterations} prime numbers of {size} bits...")
        print("Miller-Rabin")
            
        for _ in range(0, number_iterations):
            start_time = time()
            prime_number = FindPrimeNumberWithSpecificSize(size, MillerRabin.testPrimality, 32, lcg)
            end_time = time()
            iterations_time.append(end_time - start_time)

        end_time_all_primes = time()
        print(f"Average Time Miller-Rabin: {(end_time_all_primes - start_time_all_primes)/number_iterations}s")
        print(f"All measured times: {iterations_time}")
        print("-------------------------------------------------------------")
        print()

