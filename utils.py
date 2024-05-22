from collections.abc import Callable
from crypto_library.PseudoRandomNumberGenerator import *
from crypto_library.VerifyPrimality import *

def RandomNumberWithSpecificSize(expected_output_size: int, size_output_number_generator: int, number_generator: RandomNumberGenerator) -> int:

    remaining_bits = expected_output_size
    output_number = '0b'

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


def FindPrimeNumberWithSpecificSize(number_size: int, generated_number: int, used_function: Callable[[None], str], number_rounds: int = 5) -> int:
    # used_function is instance of PrimalityTester
    #TODO: ignore test of numbers that end in 5?
    #TODO: parallel programming?
    if (generated_number % 2 == 0):
        generated_number += 1
    original_number = generated_number
    maybe_prime_number = generated_number
    offset = 2

    while True:
        if (maybe_prime_number.bit_count() > number_size):
            offset = -2
            maybe_prime_number = original_number + offset

        if (used_function(maybe_prime_number, number_rounds) == "Probably prime"):
            #TODO: test if it is prime indeed with root of n
            return maybe_prime_number
        maybe_prime_number += offset
        print(f"TESTANDO: {maybe_prime_number}")
