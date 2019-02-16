

class Zombie:
    def __init__(self,speed,size,word,location):
        self.speed = speed
        self.size = size
        self.word = word
        self.location = location

    def changeSpeed(self,newSpeed):
        self.speed = newSpeed

    def changeSize(self,newSize):
        self.size = newSize

    def changeWord(self, newWord):
        self.word = newWord

    def changeLocation(self, newLocation):
        self.location = newLocation