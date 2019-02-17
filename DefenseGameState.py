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
        self._highestScore = 0
        self._currentScore = 0
        self._zombieSpeed = 0.005
        self._zombies = []
        
        self._inputStr = ""
        
        
        self._life = 3
        self._isAlive = True

        self._peterIndex = 0
        self._activateBolt = False
        
        self._shop = None

    def peterIndex(self):
        return self._peterIndex % 4

    def activateBolt(self):
        return self._activateBolt

    def reverseBolt(self):
        self._activateBolt = not self._activateBolt
    
    def updatePeterIndex(self):
        index = self._peterIndex
        self._peterIndex += 1
        # mod 4 -> 4 is number of peter images
        return index % 4

    def player(self) -> Player.Player:
        ''' Return Player Class '''
        return self._player

    def loadZombie(self) -> Zombie.Zombie:
        '''Return Zombie'''
        self._zombies.append(Zombie.Zombie(self._zombieSpeed))

    def zombieInvade(self):
        '''Remove zombie if next zombie in queue is at castle door coordinate'''
        if len(self._zombies)> 0 and self._zombies[0].top_left()[0] <= .09:
            self._removeZombie()
            self.decLife()

    def _removeZombie(self):
        '''Removes a zombie from zombie list a.k.a) zombie died
            queue style implementation'''
        self._inputStr = ""
        self._zombies.remove(self._zombies[0])

    def getZombies(self) -> "list of zombies":
        return self._zombies

    def check_character(self, charKey):
        ''' Checks the valid character in the Zombie[0] '''
        if len(self._zombies) > 0:
            needMatch = self._zombies[0].getWordProblem()
            if needMatch.checkIfSolved():

                if charKey == "return":
                    self.reverseBolt()
                    self._zombies[0].reverseShocked()
                    self._inputStr = ""
                    self._zombieSpeed += 0.00350
                    self.changeZombiesSpeed(self._zombieSpeed)
                else:
                    needMatch.makeSolZero()
                    self._inputStr = ""
                    self.changeZombiesSpeed(0.005)
            else:
                needMatch.inputChar(charKey)
                self._inputStr += charKey
                if needMatch.ZeroSolvedChar():
                    self._inputStr = ""
                    self.changeZombiesSpeed(0.005)

    def changeZombiesSpeed(self, speed):
        for i in self._zombies:
            i.changeSpeed(speed)

    def checkEqualWord(self):
        if len(self._zombies) > 0:
            return self._inputStr == self._zombies[0].getWordProblem().word()

    def gethighScore(self):
        '''Return Highest Score'''
        return self._highestScore

    def getcurrentScore(self):
        ''' Return Current Score '''
        return self._currentScore

    def incScore(self):
        self._currentScore += len(self._zombies[0].getWordProblem().word())

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

    def checkHighScore(self):
        if self._currentScore > self._highestScore:
            self._highestScore = self._currentScore

