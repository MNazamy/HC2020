from Library import Library
from Book import Book

def calcScore( tempLib, bookScores):
    score =0 
    for i in range ( len(tempLib["BooksArray"])):
        score += int(bookScores[i] )
    
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

Libraries = {}

for i in range (numLibraries):
    tempLib = {}
    line = f.readline()
    words = line.split(" ")
    tempLib["id"] = i
    tempLib["NumBooksInThisLibrary"] = words[0]
    tempLib["SignupProcess"] = words[1]
    tempLib["BooksPerDay"] = words[2]
    line = f.readline()
    books = line.split(" ")
    tempLib["BooksArray"] = books
    tempLib["Score"] = calcScore(tempLib, bookScores)

    lib = Library(tempLib)
    lib.print()








    