

from enum import Enum

class CentralSoundColor(Enum):
    FREE = 0
    HARD_SOUND = 1
    SOFT_SOUND = 2
    HARD_NOISE = 3
    SOFT_NOISE = 4
    HARD_SOUND_NOISe = 5
    SOFT_SOUND_NOISE = 6

class Rest(Enum):
    NO_REST = 0
    LONG = 1
    MEDIUM = 2
    SHORT = 3

class Effect(Enum):
    NO_EFFECT = 0
    DAMPFEN = 1
    ACCENT = 2
    ACCENT_REVERB = 3
    PERIODIC_RHYTHM = 4
    APERIODIC_RHYTHM = 5
    COMBINATION = 6

class Duration(Enum):
    NO_DURATION = 0
    MEDIUM = 1
    END = 2
    LONG = 3

class Accident(Enum):
    NO_ACC = 0
    SHORT_ACC = 1
    MEDIUM_ACC = 2
    LONG_ACC = 3
    FREE_ACC = 4

class Change(Enum):
    NO_CHANGE = 0
    INCREASE = 1
    DECREASE = 2


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
        self.CentralSound = CentralSoundColor.FREE
        self.Soundtype = 0
        # Accessories
        self.AccessoryPreTop = Accident.NO_ACC
        self.AccessoryPreBottom = Accident.NO_ACC
        self.AccessoryMidTop = Accident.NO_ACC
        self.AccessoryMidBottom = Accident.NO_ACC
        self.AccessoryPostTop = Accident.NO_ACC
        self.AccessoryPostBottom = Accident.NO_ACC
        # Subsidiary notes
        self.SubsidiariesNumber = 0
        self.SubsidiariesSpeed = 0
        self.SubsidiariesPosition = 0
        # Effect and duration
        self.Effect = Effect.NO_EFFECT
        self.Rest = Rest.NO_REST
        self.Duration = Duration.NO_DURATION
        # Tendency
        self.ChangeNumber = 0
        self.ChangeDirection = Change.NO_CHANGE
        # Flags
        self.Flags = False
        self.FlagPlus = 0
        self.FlagMinus = 0
        # coordination
        self.CoordinationTiming = 0
        self.CoordinationPitch = 0
        # connection with notepages
        self.NotePageNumber = 0
        self.Chord_nr = 0 # should be the same as the Soundtype
        self.Sequence = []
        # choices
        self.Change_possibilities = []
        self.Original_change_direction = Change.NO_CHANGE
        self.Combi_Effect = [Effect.NO_EFFECT,Effect.NO_EFFECT]

    def __repr__(self):
        return f"\n Square nr {self.squareNumber} of Symbolpage nr {self.symbolPageNumber}"

    def print_square(self):
        return f"\n " \
               f"\n "

    def make_sequence(self):
        # define self.sequence list
        # get_chord_notes
        # get_subs_notes
        # make sequence based on accidents, centralsound and subs
        pass

    def get_chord_notes(NotePageNumber, Chord_nr):
        # get the chord notes
        # return chord
        pass

    def get_subs_notes(NotePageNumber, SubsidiariesNumber):
        # get the subsidiary notes
        # return melody
        pass

    def play_sequence(sequence):
        # play the sequence
        # simulate first with printing
        # return print("ready")
        pass


