from utils import getXYs, plot, idxToXY
from pathlib import Path
import heapq
from typing import DefaultDict, List, Tuple, Dict
import math
import pprint, sys

CONSTANT = 16.67
CONSTANT2 = 16.66
def tsp_greedy(xToyList:DefaultDict[float,List[float]]):
    x0 = next(iter(xToyList)) 
    y0 = xToyList[x0][0]
    h = [(0, (x0,y0))]
    totalDist = 0
    pathPoints = []
    while h:
        dist, (x0,y0) = heapq.heappop(h)
        print(f"x0,y0: {x0},{y0}")
        totalDist+=dist
        totalDist = round(totalDist, 2)
        print(f"dist so far {totalDist}")
        pathPoints.append((x0,y0))
        h[:] = []
        yList = xToyList[x0]
        maxDist = -math.inf 
        maxY = None
        while yList:
            y = yList.pop()
            if y==y0:
                continue
            dist = math.fabs(y - y0)
            dist = round(dist, 2)
            heapq.heappush(h, (dist, (x0,y)))

            if dist > maxDist:
                maxDist = dist
                maxY = y
        xToyList.pop(x0)
        # x = next(iter(xToyList))
        if xToyList:
            x = next(iter(xToyList))
                
        if not maxY:
            if x==x0:
                continue
            print(f"1 x {x}") 
            yList = xToyList[x]
            for y in yList:
                dist = math.dist((x0,y0), (x,y))
                dist = round(dist,2)
                heapq.heappush(h, (dist, (x,y)))
        else:
            maxX = x0 + maxDist
            keylist = list(xToyList.keys())
            keyNum = 0
            print(f"2 x {x}") 
            print(f"maxDist {maxDist}")
            print(f"maxX {maxX}")
            while math.fabs(x - maxX) < 1e-5 or x < maxX:
                if x==x0:
                    break
                yList = xToyList[x]
                for y in yList:
                    dist = math.dist((x0,y0), (x,y))
                    # dist = round(dist,2)
                    heapq.heappush(h, (dist, (x,y)))
                keyNum+=1
                if xToyList and keyNum <= len(keylist)-1:
                    x = keylist[keyNum]
                else: 
                    return totalDist, pathPoints
        pprint.pprint(h)
    return totalDist, pathPoints


def tsp_greedy_brute(idxToXys: Dict[int, Tuple[float, float]], xyToIdx: Dict[int, Tuple[float, float]]):
    roundAll = lambda x,y: (round(x,2), round(y,2))
    x0,y0 = idxToXys[1.0]
    # x0,y0 = roundAll(x0,y0)

    points = []
    idx = xyToIdx[(x0,y0)]
    points.append(idx)

    visited = set()

    totalDist = 0
    paths = [(x0,y0)]
    while points:
        idx = points.pop()
        visited.add(idx)

        minDist = math.inf
        minDistPointIdx = None
        for idx2 in idxToXys.keys():
            if idx2 not in visited:
                x,y = idxToXys[idx] 
                x2,y2 = idxToXys[idx2] 

                dist = (x-x2)**2 + (y -y2)**2
                if dist<minDist:
                    minDist = dist
                    minDistPointIdx = idx2
        if minDistPointIdx:
            points.append(minDistPointIdx)
            totalDist += math.sqrt(minDist)
            paths.append(idxToXys[minDistPointIdx])

    dist = math.dist(paths[-1], paths[0]) 
    totalDist += dist
    return totalDist, paths
                
    




if __name__=="__main__":
    root = Path.home() / "work/algorithms_illuminated/npHard/test_cases/tsp_greedy"
    fname = "input_simple_21_40.txt"
    fname = "input_simple_14_10.txt"
    fname = "input_simple_30_100.txt"
    fname = "input_simple_64_10000.txt"
    fname = "tsp_greedy.txt"
    fpath = root / fname
    xys, xyDict, xToyList = getXYs(str(fpath),t="small")
    # pprint.pprint(xToyList)

    # pprint.pprint(xyDict)
    idxToXys =  idxToXY(xyDict=xyDict)
    # pprint.pprint(idxToXys)
    # totalDist, path = tsp_greedy(xToyList)
    
    totalDist, path = tsp_greedy_brute(idxToXys=idxToXys, xyToIdx=xyDict)
    print(f"totalDist: {totalDist}")
    print(f"path len {len(path)}")
    # print(path)