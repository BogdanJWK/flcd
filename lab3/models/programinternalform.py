class PIF:
    def __init__(self):
        self.__data = []

    def add(self, token, position):
        self.__data.append((token, position))

    def __str__(self):
        result = ""
        for pair in self.__content:
            result += pair[0] + "->" + str(pair[1]) + "\n"
        return result