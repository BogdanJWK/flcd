from models.hashtable import HashTable

class SymbolTable:
    
    def __init__(self, size):
        self.__hashTable = HashTable(size)
    
    def __str__(self):
        return "Symbol Table:\n" + str(self.__hashTable)

    def contains(self, e):
        return self.__hashTable.contains(e)

    def add(self, e):
        return self.__hashTable.add(e)
    
    def remove(self, e):
        return self.__hashTable.remove(e)

    def position(self, e):
        return self.__hashTable.position(e)