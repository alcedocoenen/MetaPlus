

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

    # input:
    """
    "pagenumber": 0,
    "sequencenr": 1,
    "real_number": 2,
    "boldness": 3,
    "brackets": 4,
    "centralsound": 5,
    "duration": 6,
    "rest": 7,
    "pre-bot": 8,
    "pre-top": 9,
    "mid-bot": 10,
    "mid-top": 11,
    "post-bot": 12,
    "post-top":13,
    "neben_position": 14,
    "neben-number": 15,
    "neben-speed": 16,
    "flag-top": 17,
    "flag-bottom": 18,
    "coord-timing": 19,
    "coord-pitch": 20,
    "increase": 21,
    "decrease": 22,
    "effect": 23,
    "type": 24
    """
    def __init__(self, pageNumber, squareNumber, visibleNumber, boldness, brackets, centralsound, duration, rest, pre_bot, pre_top, mid_bot, mid_top, post_bot, post_top, neben_position, neben_number, neben_speed, flag_top, flag_bottom, coord_timing, coord_pitch, increase, decrease, effect, soundtype):
        self.type = defineType(self)
        # Square id's
        self.squareNumber = squareNumber
        self.VisibleNumber = visibleNumber
        # references
        self.symbolPageNumber = pageNumber
        # square features
        self.Boldness = boldness
        self.Brackets = brackets
        # Central sound
        self.CentralSound = centralsound
        self.Soundtype = soundtype
        # Accessories
        self.AccessoryPreTop = pre_top
        self.AccessoryPreBottom = pre_bot
        self.AccessoryMidTop = mid_top
        self.AccessoryMidBottom = mid_bot
        self.AccessoryPostTop = post_top
        self.AccessoryPostBottom = post_bot
        # Subsidiary notes
        self.SubsidiariesNumber = neben_number
        self.SubsidiariesSpeed = neben_speed
        self.SubsidiariesPosition = neben_position
        # Effect and duration
        self.Effect = effect
        self.Rest = rest
        self.Duration = duration
        # Tendency
        self.Increase = increase
        self.Decrease = decrease
        # Flags
        self.FlagTop = flag_top
        self.FlagBottom = flag_bottom
        # coordination
        self.CoordinationTiming = coord_timing
        self.CoordinationPitch = coord_pitch

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


