from pathlib import Path
from collections import defaultdict
import pprint

class CustomDict(dict):
    def __setitem__(self, key, value) -> None:
        if key in self:
           return 
        return super().__setitem__(key, value)

def createGraph(fname:str):
    graph = defaultdict(list)
    with open(fname,"r") as f:
        for i,line in enumerate(f):
            if i==0:
                totalNum = int(line)
            x = tuple(map(int, line.split()))
            if len(x)==1:
                x = next(iter(x))
                graph[x].append(None)
            else:
                x1, x2 = x
                graph[x1].append(x2)
                graph[x2].append(x1)
    return graph


def getNumSet(fname: str):
    numSet = set()
    with open(fname, "r") as f:
        for i,line in enumerate(f):
            if i==0:
                totalNum = int(line)
            x = tuple(map(int, line.split()))
            if len(x)==1:
                x = next(iter(x))
                numSet.add(abs(x))
            else:
                x1, x2 = x
                numSet.add(abs(x1))
                numSet.add(abs(x2))
    return numSet

def getSetAndList(fname):
    literalsList = []
    clausesDict = CustomDict()
    literalsNumToIdx = defaultdict(list)
    literalTobitDict = {}
    idx = 0

    with open(fname, "r") as f:
        for i,line in enumerate(f):
            if i==0:
                totalNum = int(line)
            x = list(map(int, line.split()))
            if len(x)==1:
                x = next(iter(x))
                literalsNumToIdx[x].append(idx)
                literalTobitDict[x]=0 if x>0 else 1
                literalsList.append((x,))
                clausesDict[(x,)] = literalTobitDict[x]
                idx += 1
            else:
                x1, x2 = x
                literalsNumToIdx[x1].append(idx)
                literalTobitDict[x1]=0 if x1>0 else 1
                literalsNumToIdx[x2].append(idx)
                literalTobitDict[x2]=0 if x2>0 else 1
                clausesDict[(x1,x2)] =  literalTobitDict[x1] or literalTobitDict[x2]
                idx+=1
                literalsList.append((x1,x2))
    return literalsList, literalsNumToIdx, literalTobitDict, clausesDict





def getClausesAndLiterals(fname):
    clausesDict = CustomDict()
    # literalsNumToIdx = CustomDict()
    literalsNumToIdx = defaultdict(list)
    literalsList = []
    idx = 0
    numsSet = set()
    with open(fname, "r") as f:
        for i,line in enumerate(f):
            if i==0:
                totalNum = int(line)
            x = list(map(int, line.split()))
            if len(x)==1:
                x = next(iter(x))
                literalsNumToIdx[x].append(idx)
                literalsList.append(x)
    
                clausesDict[(x,)] = 0
                idx += 1
            else:
                x1, x2 = x
                idx1, idx2 = idx, idx+1
                literalsNumToIdx[x1].append(idx1)
                literalsNumToIdx[x2].append(idx2)

                literalsList.append(x1)
                literalsList.append(x2)

                clausesDict[(x1,x2)] = 0
                idx+=2
    return clausesDict, literalsNumToIdx, literalsList

def swapKeyValClausesDict(clausesDict):
    newDict = defaultdict(list)
    for k,v in clausesDict.items():
        newDict[v].append(k)
    return newDict

if __name__=="__main__":
    p = Path.home()/"work/algorithms_illuminated/npHard/test_cases/local_search"
    fname = "2sat1.txt"
    fname = "input_beaunus_10_20.txt"
    fname = p/fname

    # numsSet = getNumSet(fname)
    # pprint.pprint(numsSet)

    # clausesDict, literalsNumToIdx, literalsList = getClausesAndLiterals(str(fname))
    # pprint.pprint(clausesDict)
    # pprint.pprint(literalsNumToIdx)
    # print(literalsList)

    literalsList, literalsNumToIdx, literalBitDict, clausesDict = getSetAndList(fname)
    pprint.pprint(literalsNumToIdx)
    print(literalsList)
    pprint.pprint(literalBitDict)
    pprint.pprint(clausesDict)

    bitToClauseDict = swapKeyValClausesDict(clausesDict)
    print(bitToClauseDict)

    # graph = createGraph(fname)
    # pprint.pprint(graph)

