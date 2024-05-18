from collections.abc import Iterator

class LinearCongruentialGenerator:
    
    def __init__(self, Xo: int, m: int, a: int, c: int) -> None:
        assert all(isinstance(i, int) for i in (Xo, m, a, c)
                   ), f"Parameters must be all integers. Value at failure: {Xo}, {m}, {a}, {c}"

        self.__Xn = Xo
        self.__m = m
        self.__a = a
        self.__c = c

    def generateNumber(self) -> int:
        self.__Xn = (self.__a * self.__Xn + self.__c) % self.__m

        return self.__Xn


    def generateGenerator(self, number: int) -> Iterator[int]:
        assert(isinstance(number, int)), f"Input should be an integer. Failed value: {number}" 
        count = 0
        while count < number:
            count += 1
            self.__Xn = (self.__a * self.__Xn + self.__c) % self.__m

            yield self.__Xn