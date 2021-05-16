import MetaPlus


class makeScorePhase1():
    def __init__(self, originalScore, numberOfLayers, mapping):
        self.originalScore = originalScore # this is the complete score class instance inluding all subclasses (?)
        self.numberOfLayers = numberOfLayers
        self.mapping = mapping # a list of numbers, defines the order of Notepages
    # FIXME define the makeScorePhase1 class; is meant to create a ScorePhase1 class instance on the basis of a Score class instance


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
        # FIXME nu nog alle Note elements. Misschien terugbrengen tot alleen Notes?


