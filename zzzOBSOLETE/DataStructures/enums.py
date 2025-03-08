
class PageType(Enum):
    SYMBOLPAGE = 0
    NOTEPAGE = 1


class CentralSoundColor(Enum):
    FREE = 0
    HARD_SOUND = 1
    SOFT_SOUND = 2
    HARD_NOISE = 3
    SOFT_NOISE = 4
    HARD_SOUND_NOISE = 5
    SOFT_SOUND_NOISE = 6

class Boldness(Enum):
    NO_BOLDNESS = 0
    BOLD = 1

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