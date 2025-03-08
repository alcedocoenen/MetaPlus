# ONTOLOGIES for Symbol Pages
# all constant data expressed as tuples


# SoundColor ==========================================
SoundColorsList = [1, 2, 3, 4, 5, 6, 7]
SoundColorsList[1] = "hard sound"
SoundColorsList[2] = "soft sound"
SoundColorsList[3] = "hard noise"
SoundColorsList[4] = "soft noise"
SoundColorsList[5] = "hard sound-noise"
SoundColorsList[6] = "soft sound-noise"
SoundColorsList[0] = "free"
SoundColors = tuple(SoundColorsList)

# for x in SoundColors:
#  print(x)

# Boldness ==============================================
BoldnessList = [1, 2]
BoldnessList[0] = False
BoldnessList[1] = True
Boldness = tuple(BoldnessList)

# Brackets ================================================
BracketsList = [1, 2]
BracketsList[0] = False
BracketsList[1] = True
Brackets = tuple(BracketsList)

# Rest ========================================================
RestList = [1, 2, 3, 4]
RestList[0] = "no rest"
RestList[1] = "long"
RestList[2] = "medium"
RestList[3] = "short"
Rest = tuple(RestList)

# Duration
# only if Rest = "no rest"
Duration = ("no duration", "medium", "end", "long")

# Effect
Effect = ("no effect", "Dampfen", "Accent", "Accent-reverb", "Periodic Rhythm", "a-Periodic Rhythm", "Combination")

# SyncTiming
SyncTiming = ("no sync", "simultaneous 1", "simultaneous 2", "simultaneous 3-4", "simultaneous 5-6", "simultaneous next", "simultaneous between")

# SyncPitch
SyncPitch = ("no sync", "replace 1", "replace many", "change 1", "change many", "dynamics 1", "dynamics average")

# Accessory
Accessory = ("empty", "short", "medium", "long", "free")

# Subsidiary Position
SubsPosition = ("no subs", "pre", "medium", "post")

# Subsidiary Number
# if SubsPosition = "no subs" then SubsNumber = 0
SubsNumber = (1, 2, 3, 4, 5, 6)

# Subsidiary Speed
# if SubsPosition = "no subs" then SubsSpeed = 0
SubsSpeed = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

# Change Direction
ChangeDir = ("<", ">", "><")

# Change Value
ChangeValue = (1, 2, 3, 4, 5, 6, 7)

# Flag or not
Flag = (True, False)

# Flag Value
# if Flag = True
FlagMinus = (0, -1, -2)
FlagPlus = (0, 1, 2)

# ==== Page attributes

# Arrows
# ArrowList = ArrowPosition, ArrowDirection, ArrowNumber

ArrowPosition = ("left", "right", "left-or-right")
ArrowDirection = ("<=", "=>")
ArrowNumber = (0, 1, 2, 3)


# Brackets and empty squares
