
from collections import defaultdict
import math
import random
from utils import getSetAndList, swapKeyValClausesDict
from removeRedundants import getReducedClauses
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
        zeroClausesSet = set()
        for j in range(2*n**2):
            zeroClauses = getZeroClause(clausesDict)
            
            if zeroClauses:
                zeroClause = zeroClauses.pop()
                if zeroClause not in zeroClausesSet:
                    zeroClausesSet.add(zeroClause)
                else:
                    break
                # print(f"popped {zeroClause}")
                literal = random.choice(zeroClause)

                literalBitDict = flipBit(literal, literalBitDict)
                
                clausePositions = findClausesFromList(literal, literalsNumToIdx)
                clausesDict = evaluateClausesFromNewBitDict(clausePositions, literalsList, literalBitDict)
            else:
                return 1, literalBitDict, clausesDict

    return 0, literalBitDict, clausesDict

def separatePosNegLiterals(literalBitDict):
    literalsSet = set(literalBitDict.keys())
    posLiterals = []
    negLiterals = []
    for literal in literalsSet:
        if literal > 0:
            posLiterals.append(literal)
        else:
            negLiterals.append(literal)
    return posLiterals, negLiterals

def selectSingleSignedLiterals(posLiterals, negLiterals):
    posLiterals = set(posLiterals)
    negLiterals = set(negLiterals)
    singleSignedLiterals = []
    
    for posLiteral in posLiterals:
        if -posLiteral not in negLiterals:
            singleSignedLiterals.append(posLiteral)
    
    for negLiteral in negLiterals:
       if -negLiteral not in posLiterals:
           singleSignedLiterals.append(negLiteral)
    return singleSignedLiterals
    
def removeRedundantLiterals(clausesDict, redundantLiterals):
    redundantLiterals = set(redundantLiterals)
    keys = list(clausesDict.keys()) 
    for key in keys:
        if len(key)==1:
            x = next(iter(key))
            if x in redundantLiterals:
                clausesDict.pop(key)
        else:
            x1, x2 = key
            if x1 in redundantLiterals or x2 in redundantLiterals:
                clausesDict.pop(key)
    return clausesDict

def getLiteralsList(clausesDict, literalBitDict):
    literalsList = []
    literalsNumToIdx = defaultdict(list)

    for idx, clause in enumerate(clausesDict):
        literalsList.append(clause)
        k1,k2 = clause
        if k1 in literalBitDict:
            literalsNumToIdx[k1].append(idx)
        if k2 in literalBitDict:
            literalsNumToIdx[k2].append(idx)
    
    return literalsList, literalsNumToIdx

if __name__=="__main__":
    p = Path.home()/"work/algorithms_illuminated/npHard/test_cases/local_search"
    fname = "small.txt"
    fname = "input_beaunus_1_2.txt"
    fname = "input_beaunus_11_40.txt"
    fname = "input_beaunus_13_80.txt"
    fname = "input_beaunus_23_1000.txt"
    fname = "2sat1.txt" #1
    fname = "2sat2.txt" #0
    fname = "2sat3.txt" #0
    fname = "2sat4.txt" #0
    # fname = "2sat6.txt" #0
    # fname = "2sat5.txt" #0
    # fname = "input_beaunus_10_20.txt"
    # fname = "input_beaunus_28_4000.txt"

    fname = p/fname


    literalsList, literalsNumToIdx, literalBitDict, clausesDict = getSetAndList(fname)

    clausesDict, literalBitDict = getReducedClauses(literalBitDict=literalBitDict, clausesDict=clausesDict)
    literalsList, literalsNumToIdx = getLiteralsList(clausesDict,literalBitDict)

    repetionNum = 50 
    successes = []
    # success, _ , _ =papadimitrou(literalsList, literalsNumToIdx, literalBitDict, clausesDict)
    # print(f"success {success}")

    for l in range(repetionNum):
        success, _ , _ =papadimitrou(literalsList, literalsNumToIdx, literalBitDict, clausesDict)
        # sucess, literalBitDict, clausesDict =papadimitrou(literalsList, literalsNumToIdx, literalBitDict, clausesDict)
        print(f"success {success}")
        successes.append(success)
        print(f"max success {max(successes, key = successes.count)}")
        print(f"repaet {l}")
    print(f"final max success {max(successes, key = successes.count)}")
    
    # print("bits")
    # print(literalBitDict)
    # pprint.pprint(clausesDict)

