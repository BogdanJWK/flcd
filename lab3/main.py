from models.symbols import Symbols
from models.scanner import Scanner

symbols = Symbols("token.in")
scanner = Scanner(symbols)

print(scanner.tokenize("var x = 3; y = 6;"))