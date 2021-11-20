
from models.finiteAutomata import FiniteAutomata


class Menu:
    def __init__(self, FA_const:FiniteAutomata, FA_id:FiniteAutomata):
        self.__fa_const = FA_const
        self.__fa_id = FA_id
        self.__selected_fa:FiniteAutomata = None

    def print(self, stage):
        if stage == 0:
            print('Select Finite Automata:\n \
                    0. Exit\n \
                    1. Constants\n \
                    2. Identifiers\n')
        elif stage == 1:
            print('Select option:\n \
                    1. View all states\n \
                    2. View alphabet\n \
                    3. View start states\n \
                    4. View final states\n \
                    5. View transitions\n \
                    6. Check sequence\n')

    def getCommands(self, stage):
        if stage == 0:
            return {
                '1': self._select_fa_const,
                '2': self._select_fa_id
            }
        elif stage == 1:
            return {
                '1': self._print_states,
                '2': self._print_alphabet,
                '3': self._print_start_states,
                '4': self._print_final_states,
                '5': self._print_transitions,
                '6': self._check_sequence
            }

    def run(self):
        while True:
            cmds = self.getCommands(0)
            self.print(0)
            cmd = input('>')
            if cmd == '0':
                return
            elif cmd not in cmds:
                print('Unknown command')
                continue
            cmds[cmd]()
            cmds = self.getCommands(1)
            while True:
                self.print(1)
                cmd = input('>')
                if cmd in cmds:
                    cmds[cmd]()
                    break
                print('Unknown command!')


    def _select_fa_const(self):
        self.__selected_fa = self.__fa_const

    def _select_fa_id(self):
        self.__selected_fa = self.__fa_id

    def _print_states(self):
        if self.__selected_fa is not None:
            print(self.__selected_fa.strGetStates())
        else:
            print('Invalid Finite Automata selected!')

    def _print_start_states(self):
        if self.__selected_fa is not None:
            print(self.__selected_fa.strGetStartStates())
        else:
            print('Invalid Finite Automata selected!')

    def _print_final_states(self):
        if self.__selected_fa is not None:
            print(self.__selected_fa.strGetFinalStates())
        else:
            print('Invalid Finite Automata selected!')

    def _print_alphabet(self):
        if self.__selected_fa is not None:
            print(self.__selected_fa.strGetAlphabet())
        else:
            print('Invalid Finite Automata selected!')

    def _print_transitions(self):
        if self.__selected_fa is not None:
            print(self.__selected_fa.strGetTransitions())
        else:
            print('Invalid Finite Automata selected!')

    def _check_sequence(self):
        if self.__selected_fa is not None:
            seq = input('sequence = ')
            print('OK' if self.__selected_fa.checkSequence(seq) else 'NOT OK')
        else:
            print('Invalid Finite Automata selected!')