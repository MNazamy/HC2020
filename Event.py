import Library

class Event(object):

    def __init__(self, t, lib, isEnded):
        self.time = t
        self.Library = lib
        self.isEnd = isEnded
    

    def doEvent(self):
        if self.isEnd:
            self.Library.endSignup()
        else:
            self.Library.readBooks()