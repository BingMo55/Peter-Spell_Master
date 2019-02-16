

class Zombie:
    def __init__(self,speed,size,word,location,image):
        self.speed = speed
        self.size = size
        self.word = word
        self.location = location
        self.image = image

    def changeSpeed(self,newSpeed):
        self.speed = newSpeed

    def changeSize(self,newSize):
        self.size = newSize

    def changeWord(self, newWord):
        self.word = newWord

    def changeLocation(self, newLocation):
        self.location = newLocation
    def changeSprite(self,image):
        self.image = image