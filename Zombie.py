import pygame
import WordProblem
_ZOMBIE_SPEED = 0.005
_ZOMBIE_WIDTH = 0.080
_ZOMBIE_HEIGHT = 0.080

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super(Zombie, self).__init__()
        self._width = _ZOMBIE_WIDTH
        self._height = _ZOMBIE_HEIGHT
        self._speed = _ZOMBIE_SPEED
        self.top_left_x = 1 - self._width / 2
        self.top_left_y = 0.82 - self._height / 2

        self.zombieColor = 0
        self._isShocked = False
        self._shockedIndex = 0
        
        self._word = WordProblem.WordProblem(self.top_left_x, self.top_left_y)

        self.index = 0

    def shockedIndex(self):
        return self._shockedIndex

    def chooseShockedIndex(self):
        index = self._shockedIndex % 5
        self._shockedIndex += 1
        return index

    def isShocked(self):
        return self._isShocked

    def reverseShocked(self):
        self._isShocked = not self._isShocked

    def update(self):
        ## Barrier For Now
        self.move_left()

    def chooseImageIndex(self, Images: 'List of Zombies'):
        self.index += 1
        if self.index == len(Images):
            self.index = 0
        return self.index

    def chooseImageIndex2(self, Images: 'List of Zombies'):
        self.index += 1
        if self.index == len(Images):
            self.index = 0
        return self.index


    def top_left(self) -> (float, float):
        ''' Return Position of the zombie in a tuple '''
        return (self.top_left_x, self.top_left_y)

    def getWidth(self) -> float:
        ''' Get Width '''
        return self._width

    def getHeight(self) -> float:
        ''' Get Height '''
        return self._height
    
    def getWord(self) -> str:
        ''' Get Word '''
        return self._word

    def move_left(self) -> None:
        ''' Zombie Move to Left '''
        self._move(-self._speed)
        
    def changeSpeed(self,newSpeed):
        ''' Change Speed '''
        self._speed = newSpeed

##    def changeWord(self, newWord):
##        ''' Change Word '''
##        self._word = newWord
        
    def _move(self, delta_x: float) -> None:
        ''' Zombie Move (Private Function)'''
        tl_x = self.top_left_x
        new_x = tl_x + delta_x
        self.top_left_x = new_x

    def getWordProblem(self) -> WordProblem.WordProblem:
        return self._word
        


