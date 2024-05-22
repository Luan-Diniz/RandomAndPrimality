from collections.abc import Callable
from crypto_library.PseudoRandomNumberGenerator import *
from crypto_library.VerifyPrimality import *

first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]

def RandomNumberWithSpecificSize(expected_output_size: int, size_output_number_generator: int, number_generator: RandomNumberGenerator) -> int:

    remaining_bits = expected_output_size - 1    # MSB is 1, that's why -1 in this line.
    output_number = '0b1'

    while remaining_bits != 0:
        random_number = bin(number_generator.generateNumber())[2:] # Strip off '0b'
        zeros_needed = size_output_number_generator - len(random_number)
        zeros_needed = '0' * zeros_needed
        random_number = zeros_needed + random_number

        if (remaining_bits - size_output_number_generator < 0):
            output_number += random_number[:remaining_bits] 
            remaining_bits = 0
        else:
            remaining_bits -= size_output_number_generator
            output_number += random_number

    return int(output_number, 2)

def RandomOddNumberWithSpecificSize(expected_output_size: int, size_output_number_generator: int, number_generator: RandomNumberGenerator) -> int:
    # expected_output_size - 1 because the LSB will be 1.
    number = RandomNumberWithSpecificSize(expected_output_size - 1, size_output_number_generator, number_generator)

    return int(bin(number) + '1',2)  # LSB is 1, so the number is odd

def FindPrimeNumberWithSpecificSize(number_size: int, 
                                    used_function: Callable[[None], str], size_output_number_generator: int,
                                    number_generator: RandomNumberGenerator, number_rounds: int = 5) -> int:
    # used_function is instance of PrimalityTester

    while True:
        random_number = RandomOddNumberWithSpecificSize(number_size, size_output_number_generator, number_generator)
        for prime in first_primes_list:
            if (random_number % prime == 0):
                continue
        if (used_function(random_number, number_rounds) == "Probably prime"):
            return random_number
            