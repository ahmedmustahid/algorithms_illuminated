from pathlib import Path
from utils import getSetAndList, swapKeyValClausesDict

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

def getLiteralBitDicts(clausesDict):
    literalBitDict = dict()
    literalsSet = set()
    for k in clausesDict.keys():
        k1,k2 = k
        literalsSet.add(k1)
        literalsSet.add(k2)
    for literal in literalsSet:
        if literal > 0:
            literalBitDict[literal] = 0
            if -literal in literalsSet:
                literalBitDict[-literal] = 1
        else:
            if -literal not in literalsSet:
                literalBitDict[literal] = 0
    return literalBitDict



def removeRedundantLiterals(clausesDict, redundantLiterals):
    redundantLiterals = set(redundantLiterals)
    # print(f"redundants {redundantLiterals}")
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
                # print(f"popped {key} {x1 if x1 in redundantLiterals else x2}")
    return clausesDict

def removeSingleKeys(clausesDict):
    keys = list(clausesDict.keys()) 
    singleKeys = [k for k in keys if len(k)==1]
    print(f"singleKeys {len(singleKeys)}")
    for singlekey in singleKeys:
        clausesDict.pop(singlekey)
    for singlekey in singleKeys:
        for k in clausesDict.keys():
            x1, x2 = k
            if x1==singlekey or x2==singlekey:
                clausesDict.pop(k)
    return clausesDict

def getReducedClauses(literalBitDict, clausesDict):
    redundantLiterals = [1]
    while redundantLiterals:
        posLiterals, negLiterals = separatePosNegLiterals(literalBitDict)
        redundantLiterals = selectSingleSignedLiterals(posLiterals, negLiterals)
        print(f"literalsBitDict len {len(literalBitDict)}, redundant len: {len(redundantLiterals)}")
        print(f"before clausesdict len: {len(clausesDict)}")
        clausesDict = removeRedundantLiterals(clausesDict, redundantLiterals)
        clausesDict = removeSingleKeys(clausesDict)
        literalBitDict = getLiteralBitDicts(clausesDict)
        # print(clausesDict)
        print(f"after clausesdict len: {len(clausesDict)}")

    return clausesDict, literalBitDict
 

if __name__=="__main__":
    p = Path.home()/"work/algorithms_illuminated/npHard/test_cases/local_search"
    fname = "small.txt"
    fname = "input_beaunus_1_2.txt"
    fname = "input_beaunus_11_40.txt"
    fname = "2sat4.txt"
    fname = "2sat6.txt"
    fname = "2sat5.txt"
    fname = "input_beaunus_23_1000.txt"
    fname = "2sat2.txt"
    fname = "2sat3.txt"
    fname = "input_beaunus_28_4000.txt"
    fname = "input_beaunus_10_20.txt"
    fname = "2sat1.txt"
    fname = p/fname


    literalsList, literalsNumToIdx, literalBitDict, clausesDict = getSetAndList(fname)

    clausesDict, literalBitDict = getReducedClauses(clausesDict=clausesDict, literalBitDict=literalBitDict)
 