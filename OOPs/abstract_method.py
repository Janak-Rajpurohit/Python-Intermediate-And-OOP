from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0

    @abstractmethod
    def print_vol(self):
        return 1

    pass


class rectangle(shape):
    def __init__(self, l, b):
        self.length = l
        self.breath = b

    def print_area(self):
        return self.length * self.breath

    def print_vol(self):
        return super().print_vol()

    pass


rect = rectangle(10, 5)


# print(rect.print_area())
# and print_area function is compulsorly
# to be define in each and every clas inheritating "shape" class

## can't assign member to shape class
# square=shape()  -----> gives error
