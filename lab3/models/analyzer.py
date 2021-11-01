from models.programinternalform import PIF
from models.symboltable import SymbolTable
from models.scanner import Scanner

class Analyzer:
    def __init__(self, scanner: Scanner):
        self._scanner = scanner
        self.PIF = PIF()
        self.ST = SymbolTable()

    def analyze(self, programFile):
        with open(programFile, 'r') as f:
            crtLine = 0
            for line in f:
                crtLine += 1
                tokens = self._scanner.tokenize(line)
                for i in range(len(tokens)):
                    token = tokens[i]
                    if self._scanner.isSymbol(token):
                        if token == ' ':
                            continue
                        self.PIF.add(token, (-1, -1))