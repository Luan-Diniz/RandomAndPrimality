from collections.abc import Callable
from crypto_library.PseudoRandomNumberGenerator import *
from crypto_library.VerifyPrimality import *

def RandomNumberWithSpecificSize(size: int, number_generator: RandomNumberGenerator) -> int:
    #TODO
    # return number_generator.generateNumber()
    return None


def FindPrimeNumberWithSpecificSize(generated_number: int, used_function: Callable[[None], str]) -> str:

    #TODO
    # used_function is instance of PrimalityTester

    return used_function(generated_number)