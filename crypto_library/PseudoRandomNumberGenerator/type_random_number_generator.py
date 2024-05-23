from abc import ABC, abstractmethod
from collections.abc import Iterator


class RandomNumberGenerator(ABC):

    @abstractmethod
    def generateNumber(self) -> int:
        pass

    @abstractmethod
    def generateGenerator(self, number: int) -> Iterator[int]:
        pass