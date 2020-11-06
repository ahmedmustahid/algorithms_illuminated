

from time import time
def brute_force(arr: list)->int:

    numInv=0
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                numInv+=1
    return numInv


  
arr=[1,3,5,2,4,6]
start=time()
numInv=brute_force(arr)
assert numInv==3
end=time()
print(f"total time required in brute force {end -start}")


