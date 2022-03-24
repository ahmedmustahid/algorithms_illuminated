#import pprint
import time
def slowWay(fileName):
    startTime = time.time()
    temp = 0
    l = []

    with open(fileName,"r") as f:
        for line in f:
            tail, head = line.split()
            if temp != tail:
                temp = tail
                l.append(temp)
    #print(l)
    ldict = {e:[] for e in l}
    with open(fileName,"r") as f:
        for line in f:
            tail, head = line.split()
            if tail in ldict:
                ldict[tail].append(head)

    #pprint.pprint(ldict)
    print("--- %s seconds ---" % (time.time() - startTime))


def fasterWay(fileName):

    startTime = time.time()
    temp = "1" 
    d = {temp:[]}
    with open(fileName,"r") as f:
        for line in f:
            tail, head = line.split()
            
            if temp == tail:
                d[temp].append(head)
            else:
                temp = tail
                #d = {temp:[head]}
                d[temp] = [head]
    
    #pprint.pprint(d)
    print("--- %s seconds ---" % (time.time() - startTime))


fileName ="sccChallenge.txt" 
#fileName ="test_cases/testCase1.txt" 
#slowWay(fileName)
fasterWay(fileName)
