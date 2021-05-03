import MetaPlus from OOPocScore


class makeScorePhase1():
    def __init__(self, score):
        self.score = 0
    # FIXME define the makeScorePhase1 class; is meant to create a ScorePhase1 class instance on the basis of a Score class instance
    pass

class ScorePhase1(MetaPlus):
    # FIXME class ScorePhase1 init to be defined
    # consists of SquareEvent
    pass

class LayerPhase1():
    def __init__(self, layerNumber):
        self.layerNumber = layerNumber

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




    # FIXME consist of Square elements and Note elements


