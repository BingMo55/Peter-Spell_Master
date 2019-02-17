import random
words = ["hi", "there", "random"]

_WORDPROBLEM_WIDTH = .05
_WORDPROBLEM_HEIGHT = .05

def getWord() -> str:
    '''Returns a random word'''
    index = random.randint(0, len(words) - 1)
    return words[index]

class WordProblem:
    def __init__(self, coordX, coordY):
        # word will appear above zombie, thus zombie will generate word
        self.wordCoord_X = coordX
        self.wordCoord_Y = coordY

        self._word = getWord()
        self._numberSolvedChar = 0

    def inputChar(self, char):
        '''Add to number of characters solved if character matches the character
            in the current position of the word'''
        if char == self._word[self._numberSolvedChar]:
            self._numberSolvedChar += 1
        else:
            self._numberSolvedChar = 0

    def word(self) -> str:
        '''Return the word to solve'''
        return self._word

    def width(self) -> float:
        return _WORDPROBLEM_WIDTH

    def height(self) -> float:
        return _WORDPROBLEM_HEIGHT

    def checkIfSolved(self):
        '''Make word problem solved if the word has been spelled correctly'''
        return self._numberSolvedChar == len(self._word)

    def wordCordXY(self):
        return (self.wordCoord_X, self.wordCoord_Y)

    def ZeroSolvedChar(self):
        return self._numberSolvedChar == 0
