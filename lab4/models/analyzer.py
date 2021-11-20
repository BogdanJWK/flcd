from os import error
from models.programinternalform import PIF
from models.symboltable import SymbolTable
from models.scanner import Scanner
import re

class Analyzer:
    def __init__(self, scanner: Scanner):
        self._scanner = scanner
        self.PIF = PIF()
        self.ST = SymbolTable(16)
        self.error = ''

    def analyze(self, programFile):
        with open(programFile, 'r') as f:
            crtLine = 0
            for line in f:
                crtLine += 1
                tokens = self._scanner.tokenize(line)
                if self._scanner.isComment(tokens[0]):
                    continue
                for i in range(len(tokens)):
                    token = tokens[i]
                    if token == '\n': continue
                    
                    if self._scanner.isSymbol(token):
                        if token == ' ':
                            continue
                        self.PIF.add(token, (-1, -1))
                    elif self._scanner.isIdentifier(token):
                        id = self.ST.add(token)
                        self.PIF.add("id", id)
                    elif self._scanner.isConstant(token):
                        const = self.ST.add(token)
                        self.PIF.add("const", const)
                    else:
                        self.error += 'Lexical error at token ' + token + ', at line ' + str(crtLine) + "\n"
        with open('st.out', 'w') as st:
            st.write(str(self.ST))
        with open('pif.out', 'w') as pif:
            pif.write(str(self.PIF))
        if len(self.error) > 0:
            print(self.error)
        else:
            print('No lexical errors!')