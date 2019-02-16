_PLAYER_WIDTH = .3
_PLAYER_HEIGHT = .4

class Player:
    def __init__(self):
        top_left_x = .3 - _PLAYER_WIDTH / 2
        top_left_y = .6 - _PLAYER_HEIGHT / 2

        self._top_left = (top_left_x, top_left_y)

    def top_left(self) -> (float, float):
        '''Returns tuple of form (x, y) coordinates of player'''
        return self._top_left

    def width(self) -> float:
        '''Return player width'''
        return _PLAYER_WIDTH

    def height(self) -> float:
        '''Return player height'''
        return _PLAYER_HEIGHT
