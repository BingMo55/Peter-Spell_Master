import random
words = ["hi", "there", "random"]

def getWord():
    index = random.randint(0, len(words) - 1)
    return words[index]

class WordProblem:
    def __init__(self):
        self._word = getWord()
        self._numberSolvedChar = 0
        self._isSolved = False

    def inputChar(self, char):
        if char == self._word[self._numberSolvedChar]:
            self._numberSolvedChar += 1
            self._checkIfSolved()

    def isSolved(self):
        return self._isSolved

    def _checkIfSolved(self):
        if self._numberSolvedChar == len(self._word):
            self._isSolved = True
