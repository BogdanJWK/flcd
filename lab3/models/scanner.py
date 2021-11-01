import re

from models.symbols import Symbols

class Scanner:
    def __init__(self, symbols: Symbols):
        self._symbols = symbols

    def isIdentifier(self, token):
        return re.match(r'^[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    def isConstant(self, token):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None

    def isSymbol(self, token):
        return token in self._symbols.reserved + self._symbols.separators + self._symbols.separators

    def isPartOfOperator(self, char):
        for op in self._symbols.operators:
            if char in op:
                return True
        return False

    def isPartOfSeparator(self, char):
        for op in self._symbols.separators:
            if char in op:
                return True
        return False

    def getOperatorToken(self, line, startIndex):
        token = ''
        index = startIndex

        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1

        return token, index

    def getStringToken(self, line, startIndex):
        token = ''
        quotes = 0
        index = startIndex

        while index < len(line) and quotes < 2:
            if line[index] == '\'' or line[index] == '\"':
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    def getSeparatorToken(self, line, startIndex):
        return "" + line[startIndex], startIndex + 1


    def tokenize(self, line):
        token = None
        index = 0
        tokens = []
        while index < len(line):
            if self.isPartOfOperator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.getOperatorToken(line, index)
                tokens.append(token)
                token = None  # reset token

            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token, index = self.getStringToken(line, index)
                tokens.append(token)
                token = None  # reset token

            elif self.isPartOfSeparator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.getSeparatorToken(line, index)
                tokens.append(token)
                token = None  # reset token

            elif token:
                token += line[index]
                index += 1
            else:
                token = line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens