from Book import Book
from Library import Library

def calcScore( tempLib, bookScores):
    score =0 
    for i in tempLib["BooksArray"]:
        score += i.getScore()
    
    return score


inputFile = "a_example.txt"

f = open(inputFile, "r")

firstLine = f.readline()
words = firstLine.split(" ")

numBooks = int ( words[0] )
numLibraries =int( words[1] )
numDays = int ( words[2] )


secondLine = f.readline()
bookScores = secondLine.split(" ")
books = []
for _ in range(len(bookScores)):
    books.append(Book(_, int(bookScores[_])))

Libraries = {}

for i in range (numLibraries):
    tempLib = {}
    line = f.readline()
    words = line.split(" ")
    tempLib["id"] = i
    tempLib["NumBooksInThisLibrary"] = int(words[0])
    tempLib["SignupProcess"] = int(words[1])
    tempLib["BooksPerDay"] = int(words[2])
    line = f.readline()
    tempBooks = line.split(" ")
    bookArray = []
    for _ in tempBooks:
        bookArray.append(books[int(_)])
        
    tempLib["BooksArray"] = bookArray;

    tempLib["Score"] = calcScore(tempLib, bookScores)

    lib = Library(tempLib)
    lib.print()





    