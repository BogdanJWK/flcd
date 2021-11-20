from menu import Menu
from models.symbols import Symbols
from models.scanner import Scanner
from models.analyzer import Analyzer
from models.finiteAutomata import FiniteAutomata

FA_const = FiniteAutomata('fa-inputs/constants.in')
FA_id = FiniteAutomata('fa-inputs/identifiers.in')
menu = Menu(FA_const, FA_id)
menu.run()

