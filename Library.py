class Library:

    def __init__(self, tempLib):
            self.id = int(tempLib["id"])
            self.numBooks = int(tempLib["NumBooksInThisLibrary"] )
            self.signUpProcess = int (tempLib["SignupProcess"] )
            self.booksPerDay= int( tempLib["BooksPerDay"] )
            self.books = tempLib["BooksArray"] 
            self.score = int(tempLib["Score"])
        
    def print(self):
        bookString = ""
        for i in self.books:
            bookString += str(i) + " "
        
        print("---------------------\nLibrary ID: " + str(self.id) + "\nnumBooks " + str(self.numBooks) + "\nSign Up Length " + str(self.signUpProcess) + "\n Books Shipped Per Day" + str(self.booksPerDay ) + "\n Books : " + bookString + " \n Score: " + str(self.score))

    
    def signUpScore(self):
        pass

    def calcScore(self):
        pass

    def signUp(self):
        pass

    def readBooks(self):
        pass

    def endSignUp(self):
        pass