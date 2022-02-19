class Book:
    def __init__(self, i, s):
        self.id = i
        self.score = s
    
    def getScore(self):
        return self.score

    def getID(self):
        return self.id