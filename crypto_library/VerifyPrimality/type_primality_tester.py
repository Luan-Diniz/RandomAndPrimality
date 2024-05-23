from abc import ABC, abstractmethod


class PrimalityTester(ABC):

    @abstractmethod
    def testPrimality(n: int, number_of_rounds: int = 1) -> str:
        pass