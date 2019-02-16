import random
words = ["hi", "there", "random"]
_WORDPROBLEM_WIDTH = .05
_WORDPROBLEM_HEIGHT = .05

def getWord() -> str:
    '''Returns a random word'''
    index = random.randint(0, len(words) - 1)
    return words[index]

class WordProblem:
    def __init__(self):
        # word will appear above zombie, thus zombie will generate word
        self._word = getWord()
        self._numberSolvedChar = 0
        self._isSolved = False

    def inputChar(self, char):
        '''Add to number of characters solved if character matches the character
            in the current position of the word'''
        if char == self._word[self._numberSolvedChar]:
            self._numberSolvedChar += 1
            self._checkIfSolved()

    def isSolved(self):
        '''Return True if word has been spelled correctly'''
        return self._isSolved

    def word(self):
        '''Return the word to solve'''
        return self._word

    def width(self):
        return _WORDPROBLEM_WIDTH

    def height(self):
        return _WORDPROBLEM_HEIGHT

    def _checkIfSolved(self):
        '''Make word problem solved if the word has been spelled correctly'''
        if self._numberSolvedChar == len(self._word):
            self._isSolved = True
