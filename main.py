
inputFile = "a_example.txt"

f = open(inputFile, "r")

firstLine = f.readline()
words = firstLine.split(" ")

numBooks = words[0]
numLibraries = words[1]
numDays = words[2]


secondLine = f.readline()
bookScores = secondLine.split(" ")

libraries = {}

for i in range numLibraries:
    line = f.readline()
    words = line.split(" ")
    libraries[i] = {}
    libraries[i]["NumBooksInThisLibrary"] = words[0]
    libraries[i]["SignupProcess"] = words[1]
    libraries[i]["BooksPerDay"] = words[2]
    line = f.readline()
    books = line.split(" ")
    libraries[i]["BooksArray"] = books
    