
from os import readlink


class FiniteAutomata:
    def __init__(self, q, e, q0, f, s):
        self.Q = q
        self.E = e
        self.q0 = q0
        self.F = f
        self.S = s

    def __init__(self, filename):
        self.Q = []
        self.E = []
        self.q0 = []
        self.F = []
        self.S = {}
        self.scanFile(filename)
        if not self.isValid():
            raise Exception("Invalid FA!")

    def isValid(self):
        for q0 in self.q0:
            if q0 not in self.q0: return False
        for f in self.F:
            if f not in self.Q: return False
        for key in self.S.keys():
            state = key[0]
            symb = key[1]
            dest = self.S[key]
            if state not in self.Q: return False
            if symb not in self.E: return False
            if dest not in self.Q: return False
        return True

    def checkSequence(self, seq):
        state = self.q0[0]
        for symbol in seq:
            if (state, symbol) in self.S.keys():
                state = self.S[(state, symbol)]
            else:
                return False
        if state in self.F: return True
        return False

    def scanLine(self, line: str):
        line = line.strip().split(':')
        if (len(line) != 2):
            raise Exception('Bad input data.')
        dttype = line[0].strip()
        vals = line[1].strip().split(' ')
        if dttype == 'Q': self.Q = vals
        if dttype == 'E': self.E = vals
        if dttype == 'q0': self.q0 = vals
        if dttype == 'F': self.F = vals

        

    def scanFile(self, filename):
        with open(filename, 'r') as f:
            self.scanLine(f.readline()) # Q
            self.scanLine(f.readline()) # E
            self.scanLine(f.readline()) # q0
            self.scanLine(f.readline()) # F

            line = f.readline().strip().split(':')
            if (len(line) != 2):
                raise Exception('Bad input data.')
            dttype = line[0].strip()
            if dttype != 'S':
                raise Exception('Expected S key!')
            while len(line) > 0:
                line = f.readline()
                if line == '': break
                line = line.strip().split('->')
                if len(line) != 2:
                    raise Exception('Bad relation!')
                left = line[0].replace('(', '').replace(')', '').strip().split(',')
                if len(left) != 2:
                    raise Exception('Bad left operator!')
                src = left[0].strip()
                at = left[1].strip()
                to = line[1].strip()
                self.S[(src, at)] = to

    def strGetStates(self):
        return "Q = " + str(self.Q)

    def strGetStartStates(self):
        return "q0 = " + str(self.q0)

    def strGetFinalStates(self):
        return "F = " + str(self.F)

    def strGetAlphabet(self):
        return "E = " + str(self.E)

    def strGetTransitions(self):
        s = "S = \n"
        for key in self.S.keys():
            s += '(' + key[0] + ', ' + key[1] + ') -> ' + self.S[key]
        return s
    
    def __str__(self):
         return "Q = { " + ', '.join(str(self.Q)) + " }\n" \
                "E = { " + ', '.join(str(self.E)) + " }\n" \
                "q0 = { " + str(self.q0) + " }\n" \
                "F = { " + ', '.join(str(self.F)) + " }\n" \
                "S = { " + str(str(self.S)) + " } "

