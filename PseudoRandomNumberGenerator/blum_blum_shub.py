from collections.abc import Iterator

class BlumBlumShub:

    def __init__(self, Xo: int, p: int, q: int) -> None:
        assert all(isinstance(i, int) for i in (Xo, p, q)
                   ), f"Parameters must be all integers. Value at failure: {Xo}, {p}, {q}"
        self.__Xn = Xo
        self.__Xo = Xo
        self.__p = p
        self.__q = q
        self.__M = p * q

    def generateNumber(self) -> int:
        self.__Xn = self.__Xn**2 % self.__M

        return self.__Xn

    def generateGenerator(self, number: int) -> Iterator[int]:
        assert(isinstance(number, int)), f"Input must be an integer. Value at failure: {number}"

        count = 0
        while count < number:
            count += 1
            self.__Xn = self.__Xn**2 % self.__M

            yield self.__Xn

    def getXiValue(self, i: int) -> int:
        assert(isinstance(i, int) and i >= 0), f"Input must be a non negative integer. Value at failure: {i}"
        if i == 0: 
            return self.__Xo
        
        return (self.__Xo ** (2**i % ((self.__p-1) * (self.__q-1))) % self.__M)