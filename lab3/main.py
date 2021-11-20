from models.symbols import Symbols
from models.scanner import Scanner
from models.analyzer import Analyzer

symbols = Symbols("token.in")
scanner = Scanner(symbols)
analyzer = Analyzer(scanner)

analyzer.analyze("p1.txt")