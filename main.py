from Book import Book
from Library import Library
from Event import Event
import heapq

def calcScore( tempLib, bookScores):
    score =0 
    for i in tempLib["BooksArray"]:
        score += i.getScore()
    
    return score


def requeue(pq):
    h = []
    size = len(pq)
    for _ in range(size):
        temp = heapq.heappop(pq)[1]
        heapq.heappush(h, (temp.signUpScore(), temp))
    return h
    

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

Libraries = []

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
        
    tempLib["BooksArray"] = bookArray

    lib = Library(tempLib)
    Libraries.append(lib)


total_signed_up = 0
finalLibraryList = []
activeLibraries = [] #ordered by negative reading speed
signUpQueue = [] #ordered by
signUpLeft = 0

#add the libraries to the sign-up queue ordered by their signup score
for _ in Libraries:
    heapq.heappush(signUpQueue, (_.signUpScore(), _))



startDay = signUpQueue[0][1].signUpProcess #start main process after first is library is done signing up


for D in range(numDays-startDay):
    if signUpLeft == 0 and len(signUpQueue) > 0:
        thisLibrary = heapq.heappop(signUpQueue)[1]
        heapq.heappush(activeLibraries, (thisLibrary.booksPerDay, thisLibrary))
        finalLibraryList.append(thisLibrary)
        signUpLeft = signUpQueue[0][1].signUpProcess - 1
        total_signed_up += 1
    elif len(signUpQueue) > 0:
        signUpLeft -= 1
    
    tempStore = []

    while len(activeLibraries) > 0:
        thisLibrary = heapq.heappop(activeLibraries)[1]
        tempStore.append(thisLibrary)
        thisLibrary.readBooks(D)
    
    for _ in tempStore:
        if not _.isEmpty():
            heapq.heappush(activeLibraries, (_.booksPerDay, _))

    signUpQueue = requeue(signUpQueue)

outp = "output.txt"

with open(outp) as file:
    file.write(str(total_signed_up) + "\n")
    for _ in finalLibraryList:
        file.write(_.createOutputString())

    

    