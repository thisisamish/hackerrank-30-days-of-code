class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here

    # def computeDifference(self):
    # self.__elements.sort()
    # self.maximumDifference = self.__elements[-1] - self.__elements[0]

    # or

    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)

    # End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)