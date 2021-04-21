from datetime import datetime

class Ontology_Accessory:
    short, medium, long, indeterminate = range(4)

class Ontology_CentralSound:
    hard, soft, noises hard, noises soft, sound-noises hard, sound-noises soft, indeterminate = range(7)

class TendencyEnum:
    increase, decrease = range(2)

class Ontology_arrows:
    Left, Right = range(2)

class EffectEnum:
    no-effect, muted(D), accent-and-reverb, accent, periodic-rhythm, aperiodic-rhythm, K-any-combination = range(7)

class CoordPitch:
    no-sync, replace1, replace-many, change1, change-many, dynamics1, dynamics-average = range(7)

class Ontology_Duration:
    long, medium, short, no rest, lasts until appr the middle, lasts until the end, lasts as long as possible = range(7)

class CoordTiming:
    no-sync, simultaneous1, simultaneous2, simultaneous3-4, simultaneous5-6, simultaneous_next, simultaneous_between = range(7)

class SubsPos:
    left, mid, right = range(3)











class SymbolPage(object):
    def __init__(self):
        self.PageNumber = 0
        
        self.score = None
        self.arrow = []
        self.square = []
        self.pageChangeInstruction = []
        
    # Start of user code -> properties/constructors for SymbolPage class

    # End of user code
    # Start of user code -> methods for SymbolPage class

    # End of user code

class NotePage(object):
    def __init__(self):
        self.PageNumber = 0
        
        self.score = None
        self.subsidiaryNoteGroup = []
        self.noteGroup = []
        
    # Start of user code -> properties/constructors for NotePage class

    # End of user code
    # Start of user code -> methods for NotePage class

    # End of user code

class Square(object):
    def __init__(self):
        self.SequenceNumber = 0
        self.VisibleNumber = 0
        self.Boldness = False
        self.Brackets = False
        self.CentralSound = Ontology_CentralSound.hard
        self.Duration = Ontology_Duration.long
        self.Accessory-pre-bottom = Ontology_Accessory.short
        self.Accessory-pre-top = Ontology_Accessory.short
        self.Accessory-mid-bottom = Ontology_Accessory.short
        self.Accessory-mid-top = Ontology_Accessory.short
        self.Accessory-post-bottom = Ontology_Accessory.short
        self.Accessory-post-top = Ontology_Accessory.short
        self.SubsidiariesPosition = SubsPos.left
        self.SubsidiariesNumber = 0
        self.SubsidiariesSpeed = 0
        self.FlagPlus = 0
        self.FlagMinus = 0
        self.CoordinationTiming = CoordTiming.no-sync
        self.CoordinationPitch = CoordPitch.no-sync
        self.TendencyIncrease = 0
        self.TendencyDecrease = 0
        self.Effect = EffectEnum.no-effect
        
        self.symbolPage = None
        
    # Start of user code -> properties/constructors for Square class

    # End of user code
    # Start of user code -> methods for Square class

    # End of user code

class SubsidiaryNoteGroup(object):
    def __init__(self):
        self.number = 0
        
        self.notegroup = []
        self.notePage = None
        
    # Start of user code -> properties/constructors for SubsidiaryNoteGroup class

    # End of user code
    # Start of user code -> methods for SubsidiaryNoteGroup class

    # End of user code



class Tendency(object):
    def __init__(self):
        self.direction = TendencyEnum.increase
        self.number = 0
        
        self.pageChangeInstruction = None
        
    # Start of user code -> properties/constructors for Tendency class

    # End of user code
    # Start of user code -> methods for Tendency class

    # End of user code

class MappedSquareEvent(object):
    def __init__(self):
        self.sequencenumber = 0
        self.OriginalSquarenumber = 0
        self.OriginalSymbolpage = 0
        self.OriginalNotePagenumber = 0
        self.Effect = EffectEnum.no-effect
        self.Duration = Ontology_Duration.long
        
        self.musicEvent = []
        self.layer = None
        
    # Start of user code -> properties/constructors for MappedSquareEvent class

    # End of user code
    # Start of user code -> methods for MappedSquareEvent class

    # End of user code

class Chord(object):
    def __init__(self):
        
        self.note = []
        self.mainNoteGroup = None
        
    # Start of user code -> properties/constructors for Chord class

    # End of user code
    # Start of user code -> methods for Chord class

    # End of user code

class Meta-Plus(object):
    def __init__(self):
        self.Name = ""
        self.ID = ""
        self.DateOfCreation = datetime()
        self.DateOfUpdate = datetime()
        self.Author = ""
        self.Version  = ""
        self.Description = ""
        
        
    # Start of user code -> properties/constructors for Meta-Plus class

    # End of user code
    # Start of user code -> methods for Meta-Plus class

    # End of user code

class MusicEvent(object):
    def __init__(self):
        self.sequencenr = 0
        
        self.mappedSquareEvent = None
        self.subsidiaryNoteGroup = None
        self.mainNoteGroup = None
        
    # Start of user code -> properties/constructors for MusicEvent class

    # End of user code
    # Start of user code -> methods for MusicEvent class

    # End of user code


class MainNoteGroup(object):
    def __init__(self):
        self.number = 0
        self.soundcolor = Ontology_CentralSound.hard
        
        self.musicEvent = None
        self.chord = []
        
    # Start of user code -> properties/constructors for MainNoteGroup class

    # End of user code
    # Start of user code -> methods for MainNoteGroup class

    # End of user code

class Chord(object):
    def __init__(self):
        
        self.note = []
        self.mainNoteGroup = None
        
    # Start of user code -> properties/constructors for Chord class

    # End of user code
    # Start of user code -> methods for Chord class

    # End of user code


class SubsidiaryNoteGroup(object):
    def __init__(self):
        self.number = 0
        
        self.musicEvent = None
        self.notegroup = []
        
    # Start of user code -> properties/constructors for SubsidiaryNoteGroup class

    # End of user code
    # Start of user code -> methods for SubsidiaryNoteGroup class

    # End of user code




class Gracenote(object):
    def __init__(self):
        self.pitch = 0
        
        self.note = None
        
    # Start of user code -> properties/constructors for Gracenote class

    # End of user code
    # Start of user code -> methods for Gracenote class

    # End of user code

class Notegroup(object):
    def __init__(self):
        self.legato = False
        self.tremolo = False
        
        self.note = []
        self.subsidiaryNoteGroup = None
        
    # Start of user code -> properties/constructors for Notegroup class

    # End of user code
    # Start of user code -> methods for Notegroup class

    # End of user code


class Gracenote(object):
    def __init__(self):
        self.pitch = 0
        
        self.note = None
        
    # Start of user code -> properties/constructors for Gracenote class

    # End of user code
    # Start of user code -> methods for Gracenote class

    # End of user code

class Arrow(object):
    def __init__(self):
        self.Direction = Ontology_arrows.Left
        self.Number = 0
        
        self.symbolPage = None
        
    # Start of user code -> properties/constructors for Arrow class

    # End of user code
    # Start of user code -> methods for Arrow class

    # End of user code

class PageChangeInstruction(object):
    def __init__(self):
        self.pre-condition = ""
        self.original = None
        self.new = None
        self.frequency = 0
        self.post-condition = ""
        
        self.symbolPage = None
        self.tendency = None
        
    # Start of user code -> properties/constructors for PageChangeInstruction class

    # End of user code
    # Start of user code -> methods for PageChangeInstruction class

    # End of user code



class Note(object):
    def __init__(self):
        self.pitch = 0
        self.duration = 
        self.accent = False
        self.staccato = False
        
        self.chord = None
        self.notegroup = None
        self.gracenote = []
        
    # Start of user code -> properties/constructors for Note class

    # End of user code
    # Start of user code -> methods for Note class

    # End of user code





class Note(object):
    def __init__(self):
        self.pitch = 0
        self.duration = 
        self.accent = False
        self.staccato = False
        
        self.chord = None
        self.notegroup = None
        self.gracenote = []
        
    # Start of user code -> properties/constructors for Note class

    # End of user code
    # Start of user code -> methods for Note class

    # End of user code


class MainNoteGroup(object):
    def __init__(self):
        self.number = 0
        
        self.chord = []
        self.notePage = None
        
    # Start of user code -> properties/constructors for MainNoteGroup class

    # End of user code
    # Start of user code -> methods for MainNoteGroup class

    # End of user code

class Notegroup(object):
    def __init__(self):
        self.legato = False
        self.tremolo = False
        
        self.note = []
        self.subsidiaryNoteGroup = None
        
    # Start of user code -> properties/constructors for Notegroup class

    # End of user code
    # Start of user code -> methods for Notegroup class

    # End of user code

class Layer(object):
    def __init__(self):
        self.number = 0
        
        self.realisationPhase1 = None
        self.mappedSquareEvent = []
        
    # Start of user code -> properties/constructors for Layer class

    # End of user code
    # Start of user code -> methods for Layer class

    # End of user code

class Score(Meta-Plus):
    def __init__(self):
        
        self.square = []
        self.notePage = []
        
    # Start of user code -> properties/constructors for Score class

    # End of user code
    # Start of user code -> methods for Score class

    # End of user code

class RealisationPhase3(Meta-Plus):
    pass
    # Start of user code -> properties/constructors for RealisationPhase3 class

    # End of user code
    # Start of user code -> methods for RealisationPhase3 class

    # End of user code

class RealisationPhase2(Meta-Plus):
    pass
    # Start of user code -> properties/constructors for RealisationPhase2 class

    # End of user code
    # Start of user code -> methods for RealisationPhase2 class

    # End of user code

class RealisationPhase1(Meta-Plus):
    def __init__(self):
        
        self.layer = []
        
    # Start of user code -> properties/constructors for RealisationPhase1 class

    # End of user code
    # Start of user code -> methods for RealisationPhase1 class

    # End of user code


# Start of user code -> functions/methods for Meta-Plus package

# End of user code
