from collections import deque

class HashTable:

    def __init__(self, size):
        self.__items = [deque() for _ in range(size)]
        self.__size = size

    def hash(self, e):
        sum = 0
        for chr in e:
            sum += ord(chr) - ord('0')
        return sum % self.__size

    def contains(self, e):
        return e in self.__items[self.hash(e)]

    def position(self, e):
        list = self.hash(e)
        index = 0
        for item in self.__items[list]:
            if item != e:
                index += 1
            else:
                break
        return (list, index)


    def add(self, e):
        if self.contains(e):
            return self.position(e)
        self.__items[self.hash(e)].append(e)
        return self.position(e)

    def remove(self, e):
        self.__items[self.hash(e)].remove(e)

    def __str__(self):
        txt = ""
        for i in range(self.__size):
            txt = txt + str(i) + ': ' + str(self.__items[i]) + "\n"
        return txt

