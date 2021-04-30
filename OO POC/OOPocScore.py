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

class Square():

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

class SymbolPage():

    def __init__(self, pageNumber, scoreNumber, numberOfSquares):
        self.type = defineType(self)
        self.pageNumber = pageNumber
        self.score = scoreNumber # ref to score ID
        self.arrows = []
        self.numberOfSquares = numberOfSquares
        # self.squares = []
        '''
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
       '''

    def __repr__(self):
        return f"{self.type} nr {self.pageNumber} of score nr {self.score} "


class MainNoteGroup():
    # FIXME define the MainNotegroup class => see design
    def __init__(self, pageNumber, romanNumber):
        self.pageNumber = pageNumber # reference to NotePage
        self.romanNumber = romanNumber # is the sequel number and ID of the group


class Chord():
    def __init__(self, noteGroupnumber):
        self.number = noteGroupnumber
        self.notes = [] # list of Note(); sequence not needed


class Note():
    def __init__(self, pitch, duration, accent, staccato, grace):
        self.pitch = pitch
        self.duration = duration
        self.accent = accent
        self.staccato = staccato
        self.grace = grace

    def __str__(self):
        return f"{self.pitch}"


class NoteGroup():
    def __init__(self, legato, tremolo, subsNumber):
        self.legato = legato
        self.tremolo = tremolo
        self.subsidiary = subsNumber # reference to SubsidiaryNoteGroup where it belongs to
        self.notes = [] # list of Notes # FIXME should be sequence ?


class SubsidiaryNoteGroup():
    def __init__(self, seqNumber, pageNumber):
        self.number = seqNumber
        self.pageNumber = pageNumber




class NotePage():

    def __init__(self, pageNumber, scoreNumber):
        self.type = defineType(self)
        self.PageNumber = pageNumber
        self.score = scoreNumber
        self.subsidiaryNoteGroup = []
        self.noteGroup = []

    def __repr__(self):
        return f"Notepage nr {self.PageNumber} of score nr {self.score}"


class Score(MetaPlus):

    def __init__(self, nr_of_pages, nr_of_squares, idn):
        self.type = defineType(self)
        self.idn = idn
        self.NumberOfPages = nr_of_pages
        self.NumberOfSquares = nr_of_squares

        '''
        self.symbolpages = []
        self.notepages = []
        for i in range(nr_of_pages):
            self.spage = SymbolPage(i+1, self.idn, nr_of_squares)
            self.npage = NotePage(i+1,self.idn)
            self.symbolpages.append(self.spage)
            self.notepages.append(self.npage)
        '''

class makeScore():
    # this class is meant to create the Score and subordinated classes
    # FIXME find a way to read csv files as input, or JSON as alternative
    # FIXME it should read a file and observe how many pages and squares need to be made
    pass


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

testSymbolPage = SymbolPage(5,testScore.ID,52)

#display results:
print(testScore)
print(testSymbolPage)

# FIXME Notegroups toevoegen
