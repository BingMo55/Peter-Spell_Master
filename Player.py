_PLAYER_WIDTH = .3
_PLAYER_HEIGHT = .4
#transfer -> life, score, isAlive
class Player:
    def __init__(self):
        top_left_x = .3 - _PLAYER_WIDTH / 2
        top_left_y = .6 - _PLAYER_HEIGHT / 2

        self._top_left = (top_left_x, top_left_y)
        self._score = 0
        self._life = 3
        self._isAlive = True

    def top_left(self) -> (float, float):
        '''Returns tuple of form (x, y) coordinates of player'''
        return self._top_left

    def width(self) -> float:
        '''Return player width'''
        return _PLAYER_WIDTH

    def height(self) -> float:
        '''Return player height'''
        return _PLAYER_HEIGHT

    def score(self):
        '''Return player life left'''
        return self._score

    def incScore(self):
        self._score += 1

    def decLife(self):
        self._life -= 1
        self._checkIfAlive()

    def life(self):
        '''Return player life left'''
        return self._life

    def isAlive(self):
        '''Return True if player is still alive'''
        return self._isAlive

    def _checkIfAlive(self):
        '''Change isAlive to False if character has 0 life left'''
        if self._life == 0:
            self._isAlive = False
