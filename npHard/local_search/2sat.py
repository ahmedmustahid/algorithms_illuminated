
from collections import defaultdict
import math
import random
from utils import getSetAndList, swapKeyValClausesDict
from pathlib import Path
import pprint
import sys

def randomClausesBit(clausesDict):
    for key in clausesDict.keys():
        clausesDict[key] = random.choice((0,1))
    
    return clausesDict
    
def getZeroClause(clausesDict):
    zeroClauses = []
    for k,v in clausesDict.items():
        if v==0:
            zeroClauses.append(k)
    return zeroClauses

def flipBit(literal, literalBitDict):
    literalBitDict[literal] = 1 if literalBitDict[literal]==0 else 0
    if -literal in literalBitDict:
        literalBitDict[-literal] = 0 if literalBitDict[literal]==1 else 1
    return literalBitDict

def findClausesFromList(literal,literalsNumToIdx):
    clausePositions = []
    if literal in literalsNumToIdx:
        clausePositions = literalsNumToIdx[literal]
    if -literal in literalsNumToIdx:
        clausePositions+= literalsNumToIdx[-literal]
    return clausePositions

def evaluateClausesFromNewBitDict(clausePositions, literalsList, literalBitDict):
    clausePositions = set(clausePositions)
    for clausePosition in clausePositions:
        clause = literalsList[clausePosition]
        if len(clause)==1:
            x = next(iter(clause))
            clausesDict[(x,)] = literalBitDict[x]
        else:
            x1, x2 = clause
            clausesDict[clause] = literalBitDict[x1] or literalBitDict[x2]
    return clausesDict


def papadimitrou(literalsList, literalsNumToIdx, literalBitDict, clausesDict):
    n = len(literalsList)
    logn = math.ceil(math.log2(n))

    for i in range(logn):
        clausesDict = randomClausesBit(clausesDict)
        for j in range(2*n**2):
            zeroClauses = getZeroClause(clausesDict)
            
            if zeroClauses:
                zeroClause = zeroClauses.pop()
                # print(f"zeroclause {zeroClause}")
                literal = random.choice(zeroClause)

                literalBitDict = flipBit(literal, literalBitDict)
                
                clausePositions = findClausesFromList(literal, literalsNumToIdx)
                clausesDict = evaluateClausesFromNewBitDict(clausePositions, literalsList, literalBitDict)
            else:
                return 1, literalBitDict, clausesDict

    return 0, literalBitDict, clausesDict



if __name__=="__main__":
    p = Path.home()/"work/algorithms_illuminated/npHard/test_cases/local_search"
    fname = "small.txt"
    fname = "input_beaunus_1_2.txt"
    fname = "input_beaunus_10_20.txt"
    fname = "input_beaunus_11_40.txt"
    fname = "2sat1.txt"
    fname = "2sat2.txt"
    fname = "input_beaunus_13_80.txt"
    fname = "input_beaunus_23_1000.txt"
    fname = p/fname


    literalsList, literalsNumToIdx, literalBitDict, clausesDict = getSetAndList(fname)
    # bitToClauseDict = swapKeyValClausesDict(clausesDict)
    # pprint.pprint(literalsNumToIdx)
    # print(literalsList)
    # pprint.pprint(literalBitDict)
    # pprint.pprint(clausesDict)

    sucess, literalBitDict, clausesDict =papadimitrou(literalsList, literalsNumToIdx, literalBitDict, clausesDict)
    print(f"success {sucess}")
    print("bits")
    print(literalBitDict)
    pprint.pprint(clausesDict)

