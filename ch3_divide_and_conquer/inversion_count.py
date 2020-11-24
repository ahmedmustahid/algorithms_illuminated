
from array import array
from time import time
from inspect import currentframe,getframeinfo
frameinfo=getframeinfo(currentframe())

def brute_force(arr: array)->int:

    numInv=0
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                numInv+=1
    return numInv


def merge_and_count_splitinv(arr1: array, arr2: array)->(array,int):
    
    #if arr2[0]==0:
    #    arr2.pop(0) 
    n = len(arr1)+len(arr2)
    arr_fin= array("i",[])

    i,j,splitinv=0,0,0
    
    for k in range(n):
        #checking if one of the iterators is at the end
        if i==int(len(arr1)):
            #print("inside 1st i")
            #print(locals())
            arr_fin.extend(arr2[j:])
            return arr_fin,splitinv
        elif j==int(len(arr2)):
            #arr_fin.insert(k,arr1[i])
            arr_fin.extend(arr1[i:])
            #print("inside 1st j")
            #print(f"splitinv before {splitinv}")
            #print(locals())
            #if len(arr1[i:])>1:
            #    splitinv+=len(arr1[i+1:])
            #print(f"splitinv after {splitinv}")
            return arr_fin,splitinv
       
        if arr1[i] <= arr2[j]:
            arr_fin.insert(k,arr1[i])
            i+=1
            #print("inside 2nd j")
            #print(locals())

        else:
            arr_fin.insert(k,arr2[j])
            if not arr2[j]==0:
                #print(f"in merge splitinv {splitinv}")
                splitinv+=len(arr1)-i
            j+=1
            #print("inside 2nd j")
            #print(locals())
    return arr_fin,splitinv



def sort_and_count_inv(arr):
    
    
    n=int(len(arr))
    if not n%2==0 and not n==1:
        arr.insert(0,0)
        #print(f"locals\n {locals()}")
        #sort_and_count_inv(arr) 
    if  n==1:
        #print(f"n value {len(arr)} arr {arr}")
        #print(f"locals\n {locals()}")
        return arr,0
    else:
        #print(f"locals\n {locals()}")
        leftarr,leftinv = sort_and_count_inv(arr[:int(len(arr)/2)])
        #print(f"locals\n {locals()}")
        rightarr,rightinv=sort_and_count_inv(arr[int(len(arr)/2):])
        #print(f"locals\n {locals()}")

        #if rightarr[0]==0:
        #    arr.pop(0)
        #del_zero=lambda arr:(arr.pop(0) if arr[0]==0 else arr)
        ##del_zero(leftarr)
        #del_zero(rightarr)

        mergearr, splitinv= merge_and_count_splitinv(leftarr,rightarr)
        if mergearr[0]==0:
            mergearr.pop(0)
        #del_zero(mergearr)
        #print("=="*20)
        #print(f"locals\n {locals()}")
        return mergearr,leftinv+rightinv+splitinv



if __name__=="__main__":
    #arrtest=array("i",[3,5,2])
    #arrtest=array("i",[1,3,5,2,4,6])
    #arrtest= array("i",range(1,15))
    arrtest= array("i",range(1,10000))
    arrtest.reverse()
    start=time()
    numInv=brute_force(arrtest)
    end=time()
    print(f"numInv from brute force {numInv}")
    print(f"total time required in brute force {end -start}")
    
    start=time()
    _,numInv=sort_and_count_inv(arrtest)
    #sortedarr,numInv=sort_and_count_inv(arrtest)
    end=time()
    print("numInv from sort_and_count_inv ",numInv)
    #print(f"sortedarr {sortedarr}")
    print(f"total time required in sort_and_count_inv {end -start}")
    
    
