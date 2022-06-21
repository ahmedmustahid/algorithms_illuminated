
from array import array
from time import time
import sys,re

#from inspect import currentframe,getframeinfo
#frameinfo=getframeinfo(currentframe())

def brute_force(arr: array)->int:

    numInv=0
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                numInv+=1
    return numInv


def merge_and_count_splitinv(arr1: array, arr2: array)->(array,int):
    
    n = len(arr1)+len(arr2)
    arr_fin= array("i",[])

    i,j,splitinv=0,0,0
    
    for k in range(n):
        #checking if one of the iterators is at the end
        if i==int(len(arr1)):
            arr_fin.extend(arr2[j:])
            return arr_fin,splitinv
        elif j==int(len(arr2)):
            #arr_fin.insert(k,arr1[i])
            arr_fin.extend(arr1[i:])
            return arr_fin,splitinv
       
        if arr1[i] <= arr2[j]:
            arr_fin.insert(k,arr1[i])
            i+=1

        else:
            arr_fin.insert(k,arr2[j])
            if not arr2[j]==0:
                splitinv+=len(arr1)-i
            j+=1
    return arr_fin,splitinv



def sort_and_count_inv(arr):
    
    
    n=int(len(arr))
    if not n%2==0 and not n==1:
        arr.insert(0,0)
    if  n==1:
        return arr,0
    else:
        leftarr,leftinv = sort_and_count_inv(arr[:int(len(arr)/2)])
        rightarr,rightinv=sort_and_count_inv(arr[int(len(arr)/2):])

        mergearr, splitinv= merge_and_count_splitinv(leftarr,rightarr)
        if mergearr[0]==0:
            mergearr.pop(0)
        return mergearr,leftinv+rightinv+splitinv



if __name__=="__main__":
    
    f = open("IntegerArray.txt","r")
    f=f.read()
    str_to_int= lambda lst: ([int(num) for num in lst])
    arrtest=array("i", str_to_int(re.findall(r"[-+]?\d*\.\d+|\d+", f))) 
    #arrtest=array("i",[])
    #with open("IntegerArray.txt","r") as f:
    #    for i,line in enumerate(f):
    #        arrtest.insert(i,int(line))
    #print(*arrtest,sep="\n")
    #sys.exit()
    start=time()
    _,numInv=sort_and_count_inv(arrtest)
    end=time()
    print("numInv from sort_and_count_inv ",numInv)
    print(f"total time required in sort_and_count_inv {end -start}")
    
    
