
from collections import defaultdict
import math
import random
from utils import getSetAndList, swapKeyValClausesDict
from pathlib import Path
import pprint
import sys

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


def papadimitrou(literalsList, literalsNumToIdx, literalBitDict, clausesDict):
    n = len(literalsList)
    logn = math.ceil(math.log2(n))

    for i in range(logn):
        for j in range(2*n**2):

            zeroClauses = getZeroClause(clausesDict)
            
            if zeroClauses:
                zeroClause = zeroClauses.pop()
                literal = random.choice(zeroClause)

                literalBitDict = flipBit(literal, literalBitDict)
                
                literalPositions1, literalPositions2 = None, None
                if literal in literalsNumToIdx:
                    literalPositions1 = literalsNumToIdx[literal]
                if -literal in literalsNumToIdx:
                    literalPositions2 = literalsNumToIdx[-literal]

                sys.exit() 








if __name__=="__main__":
    p = Path.home()/"work/algorithms_illuminated/npHard/test_cases/local_search"
    fname = "2sat1.txt"
    fname = "input_beaunus_10_20.txt"
    fname = p/fname


    literalsList, literalsNumToIdx, literalBitDict, clausesDict = getSetAndList(fname)
    # bitToClauseDict = swapKeyValClausesDict(clausesDict)
    # pprint.pprint(literalsNumToIdx)
    # print(literalsList)
    # pprint.pprint(literalBitDict)
    # pprint.pprint(clausesDict)

    papadimitrou(literalsList, literalsNumToIdx, literalBitDict, clausesDict)

