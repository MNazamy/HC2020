class Book:
    def __init__(self, i, s):
        self.id = i
        self.score = s
    
    def __eq__(self,other):
        return self.id == other.getId()

    def __lt__(self, other):
        if self.score == other.getScore():
            return self.id < other.id
        else:
            return self.score < other.getScore()
    
    def __gt__(self, other):
        if self.score == other.getScore():
            return self.id > other.id
        else:
            return self.score > other.getScore()

    def getId(self):
        return self.id

    def getScore(self):
        return self.score

    def setScore(self, newVal):
        self.score = newVal