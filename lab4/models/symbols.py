
class Symbols:
    def __init__(self, tokenFile):
        self.tokenFile = tokenFile
        self.reserved = []
        self.separators = []
        self.operators = []
        self.comments = []
        self.reading = ''
        
        self.readTokens()

    def readTokens(self):
        with open(self.tokenFile, 'r') as f:
            line = f.readline()
            while line:
                line = line.strip()
                if line == '$operators$':
                    self.reading = 'operators'
                elif line == '$separators$':
                    self.reading = 'separators'
                elif line == '$reserved$':
                    self.reading = 'reserved'
                elif line == '$comment$':
                    self.reading = 'comment'
                else:
                    if line == '<space>': line = ' '
                    if self.reading == 'operators':
                        self.operators.append(line)
                    elif self.reading == 'separators':
                        self.separators.append(line)
                    elif self.reading == 'reserved':
                        self.reserved.append(line)
                    elif self.reading == 'comment':
                        self.comments.append(line)
                line = f.readline()