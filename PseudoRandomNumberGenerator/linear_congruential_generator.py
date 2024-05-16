class LinearCongruentialGenerator:
    def __init__(self, Xo, m, a, c) -> None:
        self.__Xn = Xo
        self.__m = m
        self.__a = a
        self.__c = c

    def generateNumber(self):
        self.__Xn = (self.__a * self.__Xn + self.__c) % self.__m

        return self.__Xn


    def generateGenerator(self, number):
        count = 0
        while count < number:
            count += 1
            self.__Xn = (self.__a * self.__Xn + self.__c) % self.__m

            yield self.__Xn