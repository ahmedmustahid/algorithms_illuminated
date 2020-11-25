from array import array
import re,statistics



#countcompare,countcompare2,countcompare3=0,0,0
def choosepivot(arr, leftpt, rightpt):
#    return leftpt
    temparr=array("i",[arr[leftpt],arr[rightpt]])

    #get_mid_arrnum_idx= lambda arr,leftpt,rightpt:(int(len(arr[leftpt:rightpt+1])/2)-1 if 
    #                                        len(arr[leftpt:rightpt+1])%2==0 else int(len(arr[leftpt:rightpt+1])/2))
    #mid_arrnum_idx=get_mid_arrnum_idx(arr,leftpt,rightpt)
    mid_arrnum_idx=leftpt+(rightpt-leftpt)//2
    temparr.append(arr[mid_arrnum_idx])
    #med1=statistics.median(temparr)

    temparr.pop(temparr.index(min(temparr)))
    
    median= min(temparr)
    #assert med1==median
    #print(f"med1 {med1} median {median}")
    
    if median==arr[leftpt]:
        return leftpt
    elif median==arr[rightpt]:
        return rightpt
    else:
        return mid_arrnum_idx






def partition(arr, leftpt, rightpt):
#    global countcompare
#    global countcompare2
    pivot= arr[leftpt]
    i= leftpt+1
    #countcompare+=len(arr[leftpt+1:rightpt+1])
#    countcompare+=rightpt-leftpt
    
    #for j in range(leftpt+1,len(arr[leftpt+1:rightpt+1])+1):
    for count,_ in enumerate(arr[leftpt+1:rightpt+1]):

        j=count+leftpt+1
        if arr[j] < pivot:
#            countcompare2+=1
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
    arr[leftpt],arr[i-1]=arr[i-1],arr[leftpt]

    return i-1



def quicksort(arr,leftpt,rightpt):
#    global countcompare3
    if leftpt>=rightpt:
        return 0 

    else:
        
#        countcompare3+=len(arr[leftpt:rightpt+1])-1
        num=rightpt -leftpt

        i = choosepivot(arr,leftpt,rightpt)
        arr[leftpt],arr[i]=arr[i],arr[leftpt]



        j = partition(arr,leftpt,rightpt)
        left=quicksort(arr,leftpt,j-1)
        right=quicksort(arr,j+1,rightpt)

        return num+left+right

        


if __name__=="__main__":


    #f = open("input_dgrcode_14_20.txt","r")
    f = open("Quicksort.txt","r")
    f=f.read()
    str_to_int= lambda lst: ([int(num) for num in lst])
    arr=array("i", str_to_int(re.findall(r"[-+]?\d*\.\d+|\d+", f)))

    #arr=array("i",[3,8,2,5,1,4,7,6])
    #arr=array("i",[4,5,2,3,1])
    #arr=array("i",list(range(100)))
    #arr.reverse()
    #arr=array("i",[2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12])
    #arr=array("i",[7, 1, 3, 6, 2, 5, 4, 9, 8])
    #arr=array("i",[18, 17, 20, 19])
    #arr=array("i",[7, 1, 3, 6, 2, 5, 4, 9, 8])
    #arr=array("i",[8 ,2 ,4, 5, 7, 1])
    #arr=array("i",list(range(0,5)))
    #countcompare3+=len(arr[1:len(arr)-1])
    #countcompare3+=len(arr)-2
    count=quicksort(arr,0,len(arr)-1)
    print(f"total compare {count}")
    #print("countcomparetot ",countcompare)
    #print("countcomparetot2 ",countcompare2)
    #print("countcomparetot3 ",countcompare3)
    #print(*arr,sep=" ")
