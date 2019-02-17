# Import Stuff Here
import Player
import Zombie

# Gamestate of the Defense Game -> Does the


class DefenseGameState:
    def __init__(self):
        ''' Initializes the GameState '''
        self._player = Player.Player()
        # zombies list implemented as queue -> first zombie in is first zombie
        # out when a zombie dies
        self._inputStr = ""
        
        self._zombies = []
        self._shop = None

    def player(self) -> Player.Player:
        ''' Return Player Class '''
        return self._player

    def loadZombie(self) -> Zombie.Zombie:
        '''Return Zombie'''
        self._zombies.append(Zombie.Zombie())

    def zombieInvade(self):
        '''Remove zombie if next zombie in queue is at castle door coordinate'''
        if len(self._zombies)> 0 and self._zombies[0].top_left()[0] <= .09:
            self._removeZombie()

    def _removeZombie(self):
        '''Removes a zombie from zombie list a.k.a) zombie died
            queue style implementation'''
        self._zombies.remove(self._zombies[0])

    def getZombies(self) -> "list of zombies":
        return self._zombies

    def check_character(self, charKey):
        ''' Checks the valid character in the Zombie[0] '''
        if len(self._zombies) > 0:
            needMatch = self._zombies[0].getWordProblem()
            if needMatch.checkIfSolved():
                if charKey == "return":
                    self._inputStr = ""
                    self._zombies.remove(self._zombies[0])
                else:
                    needMatch.makeSolZero()
                    self._inputStr = ""
            else:
                needMatch.inputChar(charKey)
                self._inputStr += charKey
                if needMatch.ZeroSolvedChar():
                    self._inputStr = ""

        
        
