# data structures for arrows on each symbolpage

import Ontologies.Symbols as pm  # needed for pm.Arrow* constants
import Utils.Uty as util

ArrowStatementList = []


# generic statement, generates random statement
# ArrowStatement0 = (generateArrowPosition, generateArrowDirection, generateArrowNumber)
# to be defined: generate generateArrowPosition(), generateArrowDirection(), generateArrowNumber()
def generateArrowPosition():
    return pm.ArrowPosition[util.getvalue(3, 1)]


def generateArrowDirection():
    return pm.ArrowDirection[util.getvalue(2, 1)]


def generateArrowNumber():
    return pm.ArrowNumber[util.getvalue(4, 1)]


def generateArrowStatement():
    resultListAll = []
    length = util.getvalue(4, 1)
    for i in range(1, length + 1):
        resultList = []
        position = generateArrowPosition()
        # print(position)
        resultList.append(position)
        if position != "left-or-right":
            resultList.append(generateArrowDirection())
            resultList.append(generateArrowNumber())
        resultListAll.append(resultList)
    return resultListAll


def generateArrowStatementList():
    resultArrowList = []
    for i in range(0, 7):
        resultArrowList.append(generateArrowStatement())
    return resultArrowList


ArrowStatementListOriginal = []

# page 1
ArrowStatement1 = []
ArrowStatement1.append(pm.ArrowPosition[2])
ArrowStatementListOriginal.append(ArrowStatement1)

# page 2
ArrowStatement2 = []
ArrowStatement2.append("")
ArrowStatementListOriginal.append(ArrowStatement2)

# page 3
ArrowStatement3 = []
ArrowStatement3.append(pm.ArrowPosition[2])
ArrowStatement3.append((pm.ArrowPosition[0], pm.ArrowDirection[1]))
ArrowStatement3.append((pm.ArrowPosition[1], pm.ArrowDirection[0], pm.ArrowNumber[1]))
ArrowStatementListOriginal.append(ArrowStatement3)

# page 4
ArrowStatement4 = []
ArrowStatement4.append((pm.ArrowPosition[0], pm.ArrowDirection[0]))
ArrowStatement4.append((pm.ArrowPosition[1], pm.ArrowDirection[1]))
ArrowStatement4.append((pm.ArrowPosition[0], pm.ArrowDirection[1], pm.ArrowNumber[1]))
ArrowStatement4.append((pm.ArrowPosition[1], pm.ArrowDirection[0], pm.ArrowNumber[2]))
ArrowStatementListOriginal.append(ArrowStatement4)

# page 5
ArrowStatement5 = []
ArrowStatement5.append((pm.ArrowPosition[0], pm.ArrowDirection[1]))
ArrowStatement5.append((pm.ArrowPosition[1], pm.ArrowDirection[0]))
ArrowStatementListOriginal.append(ArrowStatement5)

# page 6
ArrowStatement6 = []
ArrowStatement6.append((pm.ArrowPosition[1], pm.ArrowDirection[0]))
ArrowStatementListOriginal.append(ArrowStatement6)

# page 7
ArrowStatement7 = []
ArrowStatement7.append((pm.ArrowPosition[0], pm.ArrowDirection[0]))
ArrowStatement7.append((pm.ArrowPosition[1], pm.ArrowDirection[1]))
ArrowStatementListOriginal.append(ArrowStatement7)


def defineArrowStatement(mode, page):
    if mode == 0:  # mode 0 is random, all other is according to original score
        ArrowStatementList = generateArrowStatementList()
        select = ArrowStatementList[page]
    else:
        select = ArrowStatementListOriginal[page]
    return select


# check
# print("RANDOM")
# for i in range(0,7):
#	print(defineArrowStatement(0,i)) # first the random version

# print("ORIGINAL")
# for i in range(0,len(ArrowStatementListOriginal)):
#	print(defineArrowStatement(1,i))  # then the original one


'''
arrow constants:
ArrowPosition = ("left","right", "left-or-right")
ArrowDirection = ("<=", "=>")
ArrowNumber = (0,1,2,3)

'''

