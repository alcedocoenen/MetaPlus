class MetaPlus:
    #type = "meta"

    def __init__(self, author, name, nr, description, version):
        self.Author = author
        self.Name = name
        self.ID = nr
        self.Description = description
        self.Version = version
        self.type = str(type(self))[(str(type(self)).find("."))+1:-2]

    def __str__(self):
        return f"This is type {self.type} with nr {self.ID} - {self.Name} by {self.Author} version {self.Version} "

def defineType(klasse):
    return str(type(klasse))[(str(type(klasse)).find("."))+1:-2]

class Square(MetaPlus):

    def __init__(self, squareNumber, pageNumber):
        self.type = defineType(self)
        self.squareNumber = squareNumber
        self.symbolPageNumber = pageNumber
        self.SubsidiariesNumber = 0
        self.AccessoryMidTop = 0
        self.TendencyDecrease = 0
        self.AccessoryPreTop = 0
        self.AccessoryPreBottom = 0
        self.AccessoryMidBottom = 0
        self.AccessoryPostTop = 0
        self.TendencyIncrease = 0
        self.FlagPlus = 0
        self.Effect = 0
        self.AccessoryPostBottom = 0
        self.CoordinationTiming = 0
        self.SequenceNumber = 0
        self.Brackets = False
        self.CoordinationPitch = 0
        self.SubsidiariesSpeed = 0
        self.SubsidiariesPosition = 0
        self.CentralSound = 0
        self.Duration = 0
        self.Boldness = False
        self.VisibleNumber = 0
        self.FlagMinus = 0
    def __repr__(self):
        return f"\n Square nr {self.squareNumber} of Symbolpage nr {self.symbolPageNumber}"

class SymbolPage(MetaPlus):

    def __init__(self, pageNumber, scoreNumber, numberOfSquares):
        self.type = defineType(self)
        self.pageNumber = pageNumber
        self.score = scoreNumber # ref to score ID
        self.arrows = []
        self.squares = []
        for i in range(numberOfSquares):
            self.thisSquare = Square(i+1, self.pageNumber)
            self.squares.append(self.thisSquare)
        self.pageChangeInstruction = []

    def makeSquare(self, squareNumber, pageNumber):
        newSquare = Square(squareNumber, pageNumber)
        newSquare.ID = squareNumber
        newSquare.Name = "blabla"
        newSquare.Author = "CA"
        newSquare.Version = "2.0"
        return newSquare

    def makeSquares(self, squareNumberOffset, pageNumber, numberOfSquares):
        squares = []
        for i in range(numberOfSquares):
            thisSquare = Square(squareNumberOffset + i + 1, pageNumber)
            squares.append(thisSquare)
        return squares

    def __repr__(self):
        return f"\n Symbolpage nr {self.pageNumber} of score nr {self.score} and squares \n {self.squares}"


class NotePage(MetaPlus):

    def __init__(self, pnr, scnr):
        self.type = defineType(self)
        self.PageNumber = pnr
        self.score = scnr
        self.subsidiaryNoteGroup = []
        self.noteGroup = []

    def __repr__(self):
        return f"Notepage nr {self.PageNumber} of score nr {self.score}"


class Score(MetaPlus):

    def __init__(self, nr_of_pages, nr_of_squares, idn):
        self.type = defineType(self)
        self.idn = idn
        self.symbolpages = []
        self.notepages = []
        for i in range(nr_of_pages):
            self.spage = SymbolPage(i+1, self.idn, nr_of_squares)
            self.npage = NotePage(i+1,self.idn)
            self.symbolpages.append(self.spage)
            self.notepages.append(self.npage)

    def drukaf(self):
        print(f"{self.symbolpages} and {self.notepages}")


# definition data:
scorenr = 101
score_name = "original test"
score_author = "AC"
score_version = "0.1"
number_of_pages = 3
number_of_squares = 5

#define instance of score:
testScore = Score(number_of_pages, number_of_squares, scorenr)
testScore.ID = scorenr
testScore.Name = score_name
testScore.Author = score_author
testScore.Version = score_version

#display results:
print(testScore)
testScore.drukaf()

testSquare = testScore.symbolpages[1].makeSquare(5,3)
print(testSquare)


'''
TODO
v Squares nog gereed maken
v zorgen dat vanuit Symbolpage de square worden gemaakt
* zorgen dat vanuit Notepage de notegroups worden gemaakt
* nog uitzoeken hoe je data kunt inlezen (en misschien daarvan laten afhangen hoeveel...)
* ontologiee"en toevoegen, of gewoon nummertjes houden?
* hoe benader je objecten van binnen de superclass 

* losmaken van de subclassesvan de superclass
* aparte methodes binnen de superclass om een subclass te maken, daarmee kun je ze apart benoemen en toch koppelen

'''