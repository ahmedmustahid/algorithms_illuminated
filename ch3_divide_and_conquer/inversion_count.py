
from array import array
from time import time
def brute_force(arr: array)->int:

    numInv=0
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                numInv+=1
    return numInv


def merge_and_count_splitinv(leftarr,rightarr):
    print(f"leftarr {leftarr}")
    print(f"rightarr {rightarr}")
    #breakpoint()
    n=int(len(leftarr)+len(rightarr))
    mergearr=array("f",[])

    i,j,splitinv=0,0,0

    for _ in range(n):
        print(f"i {i}")
        print(f"j {j}")
        print(f"mergearr {mergearr}")
        if leftarr[i] < rightarr[j]:
            mergearr.append(leftarr[i])
            i+=1
        else:
            mergearr.append(rightarr[j])
            j+=1
            splitinv+= n/2 - i +1

    return mergearr, splitinv




def sort_and_count_inv(arr):
    

    n=int(len(arr))
    if  n==1:
        print(f"n value {n} arr {arr}")
        return arr,0
    else:
        #breakpoint()
        #print(f"n/2 {int(n/2)} ")

        #n=int(len(arr))
        #n=int(len(arr))
        print(f"arr[:{int(n/2)}] {arr[:int(n/2)]}")
        leftarr,leftinv = sort_and_count_inv(arr[:int(len(arr)/2)])
        #n=int(len(arr))
        print(f"arr[{int(n/2)}:] {arr[int(n/2):]}")
        #n=int(len(arr))
        rightarr,rightinv=sort_and_count_inv(arr[int(len(arr)/2):])
        
        print(f"leftarr {leftarr} leftinv {leftinv}")
        print(f"rightarr {rightarr} rightinv {rightinv}")
        mergearr, splitinv= merge_and_count_splitinv(leftarr,rightarr)

        return (mergearr, leftinv+rightinv+splitinv)



  
arrtest=array("i",[1,3,5,2,4,6])
start=time()
numInv=brute_force(arrtest)
assert numInv==3
end=time()
print(f"total time required in brute force {end -start}")

start=time()
_,numInv=sort_and_count_inv(arrtest)
assert numInv==3
end=time()
print(f"total time required in sort_and_count_inv {end -start}")


