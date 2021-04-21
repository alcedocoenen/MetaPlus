"""
First setup with limited numbers of pages, squares and notes, in order to enable unit testing
The structures themselves need to be complete at the end
"""

# some set of parameters that can change in order to enlarge the set of data
# nsq = 5 # number of squares per page
# np = 3 # number of pages

# m = 0 # mode = 0 => random, mode = 1 => get real values from original score, mode = 2 => get values from specified source


import random
import Ontologies.Symbols as pm
import Operations.Replacements as repl
import Utils.Uty as util
import DataStructures.Arrows as ar


# ===== makeSquare ===========================
def makeSquare(sqnr, m):
    # quare structure contains:
    '''
        boldness
        brackets
        soundcolor
        duration
        rest
        effect
        accidents = (accPreBot,accPreTop,accCenBot,accCenTop,accPosBot,accPosTop)
        subsidiary = (subsPosition,subsNumber,subsSpeed)
        flag = (flagTop,flagBottom)
        sync = (coordinationTiming,coordinationPitch)
        change = (tendencyIncrease,tendencyDecrease)
    '''

    #	sq = [a, 5, 8] # moet vervangen worden door random generatoren of door uitlezen van records
    #	sq = [sqnr, random.randint(1,25), random.randint(75,100)] # sample random

    # some sublists within the square
    accidentsList = []
    for i in range(6):
        acc = pm.Accident[util.getvalue(len(pm.Accident), m)]
        accidentsList.append(acc)

    subsList = []
    subsPos = pm.SubsPosition[util.getvalue(len(pm.SubsPosition), m)]
    subsList.append(subsPos)
    if subsPos != 'no subs':
        subsList.append(pm.SubsNumber[util.getvalue(len(pm.SubsNumber), m)])
        subsList.append(pm.SubsSpeed[util.getvalue(len(pm.SubsSpeed), m)])

    coreEventList = []  # core event that needs to be translated into musical events
    cs = pm.SoundColorsList[util.getvalue(len(pm.SoundColorsList), m)]
    coreEventList.append(cs)
    coreEventList.append(accidentsList)
    coreEventList.append(subsList)
    rst = pm.Rest[util.getvalue(len(pm.Rest), m)]
    coreEventList.append(rst)
    dur = pm.Duration[util.getvalue(len(pm.Duration), m)]
    coreEventList.append(dur)

    changeList = []  # change signs < and > plus number
    chDir = pm.ChangeDir[util.getvalue(len(pm.ChangeDir), m)]
    chV = pm.ChangeValue[util.getvalue(len(pm.ChangeValue), m)]
    changeList.append(chDir)
    changeList.append(chV)

    flagsList = []  # flags
    flag = pm.Flag[util.getvalue(len(pm.Flag), m)]
    flagsList.append(flag)
    if flag > 0:
        pos = util.getvalue(len(pm.FlagValue), m)
        topFlag = pm.FlagValue[pos]
        flagsList.append(topFlag)  # waarom wordt dit een aparte list?
        if flag == 2:
            bottomFlag = pm.FlagValue[util.getvalue(len(pm.FlagValue), m)]
            flagsList.append(bottomFlag)

    sq = [sqnr,

          pm.Boldness[util.getvalue(len(pm.Boldness), m)],
          pm.Brackets[util.getvalue(len(pm.Brackets), m)],
          coreEventList,
          changeList,
          flagsList,
          pm.Effect[util.getvalue(len(pm.Effect), m)],
          pm.SyncTiming[util.getvalue(len(pm.SyncTiming), m)],
          pm.SyncPitch[util.getvalue(len(pm.SyncPitch), m)]
          ]

    return sq


# ===== END makeSquare ===========================


def makeSymbolPage(numberOfSquares, pagenr, mode):
    squareList = [pagenr]
    for i in range(1, numberOfSquares + 1):
        square = makeSquare(i, mode)
        squareList.append(square)

    # replacement algorithm
    # replacementStatement per page opzoeken (of random bepalen) => random moet nog gedefinieerd worden
    replStatList = repl.replacementStatementList[pagenr]
    squareList.append(replStatList)  # add replacement statement to the page itself
    # squarelist = repl.replaceChangeValues(squareList, replStatList) # this is the actual replacement function

    # arrows
    arrowStatList = ar.defineArrowStatement(mode, i)  # 0 = random choice, 1 = original score
    squareList.append(arrowStatList)  # add arrow statement to page itself

    return squareList


def makeSymbolScore(numberOfPages, numberOfSquaresPerPage, mode):
    pageList = []

    for i in range(1, numberOfPages + 1):
        page = makeSymbolPage(numberOfSquaresPerPage, i, mode)
        pageList.append(page)
    return pageList

# ==== just check ================================
# print(makeSymbolScore(np,nsq))


