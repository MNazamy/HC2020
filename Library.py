
import Event
from queue import PriorityQueue
import math

class Library:

    def __init__(self, tempLib):
            self.id = int(tempLib["id"])
            self.numBooks = int(tempLib["NumBooksInThisLibrary"] )
            self.signUpProcess = int (tempLib["SignupProcess"] )
            self.booksPerDay= int( tempLib["BooksPerDay"] )
            self.booksRead = []
            self.books = tempLib["BooksArray"] 
            self.queue = PriorityQueue()
            for book in self.books:
                self.queue.put ( (-1*book.getScore(),book ))

            self.calcScore()

    def print(self):
        bookString = ""
        for i in self.books:
            bookString += str(i.getId()) + " "
        
        printString = ( "---------------------\nLibrary ID: " + str(self.id) + "\nnumBooks " + str(self.numBooks) + "\nSign Up Length: " + str(self.signUpProcess))
        printString += ( "\nBooks Shipped Per Day: " + str(self.booksPerDay ) + "\nBooks: " + bookString + " \nScore: " + str(self.score))
        print(printString)

    def signUpScore(self):
        sur = self.signUpProcess * self.signUpProcess
        br = self.booksPerDay * self.booksPerDay
        bnum = self.numBooks * self.numBooks
        daysforallbooks = bnum/br
        bscore = self.calcScore() * self.calcScore
        scoreperday = daysforallbooks/bscore
        return (math.sqrt(scoreperday/sur))
      
    def calcScore(self):
        total = 0
        for i in self.books:
            total += i.getScore()

        self.score = total

    def signUp(self,day):
        ev = Event(day+self.signUpProcess,self, True)
        return ev

    def readBooks(self, day):
        self.updateQueue()
        for _ in range(self.booksPerDay):
            self.booksRead.append( self.queue.get()[1] )
            self.booksRead[-1].setScore(0)

        rb = Event(day+1,self,False)
        return rb

    def endSignUp(self,day):
        rb = Event(day+1,self, False)
        return rb

    def updateQueue(self):
        bookList = []
        while not self.queue.empty():
            bookList.append(self.queue.get()[1])
        
        for book in bookList:
            if book.getScore() != 0:
                self.queue.put ( (-1*book.getScore(),book ))
        
        self.calcScore()
        
    def isEmpty(self):
        return self.queue.empty()

    def createOutputString(self):
        output = "\n" + str(self.id) + " " + str(len(self.booksRead) ) + "\n"
        for book in self.booksRead:
            output += str(book.getId() + " ")
        
        return output

    def getScore(self):
        return self.score