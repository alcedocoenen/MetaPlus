# import MetaPlus
import OO_Score


class makeScorePhase1():
    def __init__(self, originalScore, numberOfLayers, mapping):
        self.originalScore = originalScore # this is the complete score class instance inluding all subclasses (?)
        self.numberOfLayers = numberOfLayers
        self.mapping = mapping # a list of numbers, defines the order of Notepages
    # FIXME define the makeScorePhase1 class; is meant to create a ScorePhase1 class instance on the basis of a Score class instance


class ScorePhase1(OO_Score.MetaPlus):
    # FIXME class ScorePhase1 init to be defined
    # consists of SquareEvent
    pass


class LayerPhase1():
    def __init__(self, layerNumber):
        self.layerNumber = layerNumber

'''
class SquareEvent():

    def __init__(self, layerNumber, eventnumber, scorenr, originalSymbolPage, originalSquarenr, originalNotePage):
        # Square id's
        self.eventnumber = eventnumber
        # references
        self.layer = layerNumber
        self.score1 = scorenr # reference to ScorePhase1
        self.originalSymbolPage = originalSymbolPage
        self.originalSquarenr = originalSquarenr
        self.originalNotePage = originalNotePage
        # Central sound
        self.CentralSound = 0
        self.CentralSoundType = 0
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
        self.Duration = 0
        # Tendency
        self.TendencyDecrease = 0
        self.TendencyIncrease = 0
        # repetitions
        self.repetitions = 1 #needs to be adjusted aoording to Plus and Minus flags
        # coordination
        self.CoordinationTiming = 0
        self.CoordinationPitch = 0
        # FIXME nu nog alle Note elements. Misschien terugbrengen tot alleen Notes?

'''

class SquareEvent():

    def __init__(self, square, notegroup, subsgroup):
        self.square = square
        self.notegroup = notegroup
        self.subsgroup = subsgroup

    def displayAll(self):
        return f"square = {self.square}, \nnotegroup = {self.notegroup}, \nsubsgroup = {self.subsgroup}"

    def defineType(self):
        # afleiden van de constellatie van accessories en centralsound
        # see instructions nr 6
        # type 1 = A -> C = (A-pre, C)
        # type 2 = AC   = (A-mid, C) # AC means A and C at the same time
        # type 3 = C -> A = (C, A-pos)
        # type 4 = A -> C -> A = (A-pre, C, A-pos)
        # type 5 = AC -> A = (A-mid, C, A-pos)
        # type 6 = A -> AC = (A-pre, A-mid, C)
        # type 7 = A -> AC -> A = (A-pre, A-mid, C, A-pos)
        w, h = 3,3
        a = [[0 for x in range(w)] for y in range(h)]
        a[0][0] = self.square.AccessoryPreTop
        a[0][1] = self.square.AccessoryPreBottom
        a[1][0] = self.square.AccessoryMidTop
        a[1][1] = self.square.AccessoryMidBottom
        a[2][0] = self.square.AccessoryPostTop
        a[2][1] = self.square.AccessoryPostBottom

        testarray = []
        for i in a:
            if (i[0] != "empty" or i[1] != "empty"):
                i[2] = True
            else:
                i[2] = False
            testarray.append(i[2])

        if (testarray == [True, False, False]):
            return 1
        elif (testarray == [False, True, False]):
            return 2
        elif (testarray == [False, False, True]):
            return 3
        elif (testarray == [True, False, True]):
            return 4
        elif (testarray == [False,True,True]):
            return 5
        elif (testarray == [True,True,False]):
            return 6
        elif (testarray == [True,True,True]):
            return 7



def makeEventSequence(self):
        # 1. pre-accessories + subs
        # 2. central-sound = chord + mid-accessories + subs
        # 3. post-accessories + subs
        microSequence1 = []
        microSequence2 = []
        microSequence3 = []

        # 1. pre-accessories
        microSequence1.append(self.square.AccessoryPreTop)
        microSequence1.append(self.square.AccessoryPreBottom)
        # subs notes, af te leiden van subsnumber

        # 2. central-sound
        microSequence2.append()


testScore = OO_Score.makeScore()
print("testScore gemaakt")
testSq = testScore.createRandomSquare(1,1,1)
print("testSquare gemaakt")
print(testSq.AccessoryPreTop)
print(testSq.AccessoryPreBottom)
print(testSq.AccessoryMidTop)
print(testSq.AccessoryMidBottom)
print(testSq.AccessoryPostTop)
print(testSq.AccessoryPostBottom)


testNg = OO_Score.makeTestNoteGroup()
print("testNotegroup gemaakt")

testSb = []
testSqEvent = SquareEvent(testSq,testNg,testSb)
print("testSqEvent gemaakt")
print(testSq)
print(testSqEvent.displayAll())
print(f"type = {testSqEvent.defineType()}")

