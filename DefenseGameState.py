# Import Stuff Here
import Player
import Zombie
import WordProblem

# Gamestate of the Defense Game -> Does the


class DefenseGameState:
    def __init__(self):
        ''' Initializes the GameState '''
        self._player = Player.Player()
        self._words = WordProblem.WordProblem()
        self._zombies = Zombie.Zombie(self._words)
        self._shop = None

    def player(self) -> Player.Player:
        ''' Return Player Class '''
        return self._player

    def words(self) -> WordProblem.WordProblem:
        ''' Return WordProblem Class '''
        return self._words

    def zombie(self) -> Zombie.Zombie:
        ''' Return Zombie Class '''
        return self._zombies
