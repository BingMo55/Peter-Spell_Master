# Import Stuff Here
import Player
import Zombie

# Gamestate of the Defense Game -> Does the


class DefenseGameState:
    def __init__(self):
        ''' Initializes the GameState '''
        self._player = Player.Player()
        self._zombies = []
        self._shop = None

    def player(self) -> Player.Player:
        ''' Return Player Class '''
        return self._player

    def loadZombie(self) -> Zombie.Zombie:
        '''Return Zombie'''
        self._zombies.append(Zombie.Zombie())

    def getZombies(self) -> "list of zombies":
        return self._zombies
