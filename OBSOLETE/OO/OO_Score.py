from Ontologies import Symbols
import random
import mido
import Midiplay

class MetaPlus:

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

    def __init__(self, squareNumber, visibleNumber, pageNumber):
        self.type = defineType(self)
        # Square id's
        self.squareNumber = squareNumber
        self.VisibleNumber = visibleNumber
        # references
        self.symbolPageNumber = pageNumber
        # square features
        self.Boldness = False
        self.Brackets = False
        # Central sound
        self.CentralSound = 0
        # Accessories
        self.AccessoryPreTop = 0
        self.AccessoryPreBottom = 0
        self.AccessoryMidTop = 0
        self.AccessoryMidBottom = 0
        self.AccessoryPostTop = 0
        self.AccessoryPostBottom = 0
        # Subsidiary notes
        self.SubsidiariesNumber = 0
        self.SubsidiariesSpeed = 0
        self.SubsidiariesPosition = 0
        # Effect and duration
        self.Effect = 0
        self.Rest = 0
        self.Duration = 0
        # Tendency
        self.ChangeNumber = 0
        self.ChangeDirection = 0
        # Flags
        self.Flags = False
        self.FlagPlus = 0
        self.FlagMinus = 0
        # coordination
        self.CoordinationTiming = 0
        self.CoordinationPitch = 0

    def __repr__(self):
        return f"\n Square nr {self.squareNumber} of Symbolpage nr {self.symbolPageNumber}"

    def print_square(self):
        return f"\n " \
               f"\n "


class SymbolPage():

    def __init__(self, pageNumber, scoreNumber, numberOfSquares):
        self.type = defineType(self)
        self.pageNumber = pageNumber
        self.score = scoreNumber # ref to score ID
        self.arrows = []
        self.numberOfSquares = numberOfSquares
        self.allSquares = []
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
    def __init__(self, pageNumber, romanNumber, chord):
        self.pageNumber = pageNumber # reference to NotePage
        self.romanNumber = romanNumber # is the sequel number and ID of the group
        self.chord = chord

    def __repr__(self):
        return f"\npagenumber = {self.pageNumber}, romanNumber = {self.romanNumber}, \nchord = {self.chord}"


class Chord():
    def __init__(self, noteGroupnumber, notes):
        self.number = noteGroupnumber
        self.notes = notes # list of Note(); sequence not needed
    def __repr__(self):
        return f"notes = {self.notes}"


class Note():
    def __init__(self, pitch, duration, accent, staccato, grace):
        self.pitch = pitch
        self.duration = duration
        self.accent = accent
        self.staccato = staccato
        self.grace = grace

    def __repr__(self):
        return f"pitch={self.pitch}, dur={self.duration}, accent={self.accent}, stacc={self.staccato}, grace={self.grace}"

    def makeJson(self):
        return f"{{\'pitch\': {self.pitch},\n \'duration\': {self.duration},\n \'accemt\': {self.accent},\n \'staccato\': {self.staccato},\n \'grace\': {self.grace} }}"

    def play(self):
        portlist = mido.get_output_names()
        portname = portlist[0]
        port = mido.open_output(portname)
        msg1 = mido.Message('note_on', note = self.pitch, time=0)
        msg2 = mido.Message('note_off', note = self.pitch, time=self.duration)
        port.send(msg1)
        port.send(msg2)


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
        self.referencePitch = 0


class NotePage():

    def __init__(self, pageNumber, scoreNumber):
        self.type = defineType(self)
        self.PageNumber = pageNumber
        self.score = scoreNumber
        self.allSubsidiaryNoteGroups = []
        self.allMainNoteGroups = []

    def __repr__(self):
        return f"Notepage nr {self.PageNumber} of score nr {self.score}"


class Score(MetaPlus):

    def __init__(self, nr_of_pages, nr_of_squares, idn):
        self.type = defineType(self)
        self.idn = idn
        self.NumberOfPages = nr_of_pages
        self.NumberOfSquares = nr_of_squares
        self.allSymbolPages = []
        self.allNotePages = []

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
    # 1. first read all squares into Square class => separate Squares.csv
    # 2. read all notes into MainNotesgroup class => separate Notes.csv
    # 3. read all page info into Pages and add squares / Notegroups => separate 
    # 4. compose Score class and add Pages

    def __init__(self):
        self.numberOfSquares = 1

    def createRandomSquare(self, squareNumber, visibleNumber, pageNumber):
        sq = Square(squareNumber, visibleNumber, pageNumber)

        # define all attributes
        sq.Boldness = Symbols.Boldness[random.randrange(0,len(Symbols.Boldness))]
        sq.Brackets = Symbols.Brackets[random.randrange(0,len(Symbols.Brackets))]
        # Central sound
        sq.CentralSound = Symbols.SoundColors[random.randrange(0,len(Symbols.SoundColors))]
        # Accessories
        sq.AccessoryPreTop = Symbols.Accessory[random.randrange(0,len(Symbols.Accessory))]
        sq.AccessoryPreBottom = Symbols.Accessory[random.randrange(0,len(Symbols.Accessory))]
        sq.AccessoryMidTop = Symbols.Accessory[random.randrange(0,len(Symbols.Accessory))]
        sq.AccessoryMidBottom = Symbols.Accessory[random.randrange(0,len(Symbols.Accessory))]
        sq.AccessoryPostTop = Symbols.Accessory[random.randrange(0,len(Symbols.Accessory))]
        sq.AccessoryPostBottom = Symbols.Accessory[random.randrange(0,len(Symbols.Accessory))]
        # Subsidiary notes
        sq.SubsidiariesPosition = Symbols.SubsPosition[random.randrange(0,len(Symbols.SubsPosition))]
        if sq.SubsidiariesPosition == "no subs":
            sq.SubsidiariesNumber = 0
            sq.SubsidiariesSpeed = 0
        else:
            sq.SubsidiariesNumber = Symbols.SubsNumber[random.randrange(0,len(Symbols.SubsNumber))]
            sq.SubsidiariesSpeed = Symbols.SubsSpeed[random.randrange(0,len(Symbols.SubsSpeed))]
        # Effect and duration
        sq.Effect = Symbols.Effect[random.randrange(0,len(Symbols.Effect))]
        sq.Rest = Symbols.Rest[random.randrange(0,len(Symbols.Rest))]
        if sq.Rest == "no rest":
            sq.Duration = Symbols.Duration[random.randrange(0,len(Symbols.Duration))]
        else:
            sq.Duration = "no duration"
        # Tendency
        sq.ChangeDirection = Symbols.ChangeDir[random.randrange(0,len(Symbols.ChangeDir))]
        sq.ChangeNumber = Symbols.ChangeValue[random.randrange(0,len(Symbols.ChangeValue))]
        # Flags
        sq.Flags = Symbols.Flag[random.randrange(0,len(Symbols.Flag))]
        sq.FlagPlus = Symbols.FlagPlus[random.randrange(0,len(Symbols.FlagPlus))]
        sq.FlagMinus = Symbols.FlagMinus[random.randrange(0,len(Symbols.FlagMinus))]
        # coordination
        sq.CoordinationTiming = Symbols.SyncTiming[random.randrange(0,len(Symbols.SyncTiming))]
        sq.CoordinationPitch = Symbols.SyncPitch[random.randrange(0,len(Symbols.SyncPitch))]

        return sq




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



def makeTestNoteGroup():

    testChord = Chord(34)
    testNotes=[]
    for i in range(7):
        testNotes.append(Note(i,i,i,i,i))
        # print(testNotes[i])

    testChord.notes=testNotes
    '''
    for i in testChord.notes:
        print(i)
    print(testChord)
    '''
    testNg = MainNoteGroup(1,1, testChord)
    #print(testNg)
    return testNg


'''
testMakeScore = makeScore()
testSq = testMakeScore.createRandomSquare(1, 1, 1)
print(testSq)
'''