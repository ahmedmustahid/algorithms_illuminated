from array import array
import re



countcompare=0
def choosepivot(arr, leftpt, rightpt):
    temparr=array("i",[arr[leftpt],arr[rightpt]])

    get_mid_arrnum_idx= lambda arr,leftpt,rightpt:(int(len(arr[leftpt:rightpt+1])/2)-1 if 
                                            len(arr[leftpt:rightpt+1])%2==0 else int(len(arr[leftpt:rightpt+1])/2))
    mid_arrnum_idx=get_mid_arrnum_idx(arr,leftpt,rightpt)
    temparr.append(arr[mid_arrnum_idx])

    temparr.pop(temparr.index(min(temparr)))
    
    median= min(temparr)

    return arr.index(median) 




def partition(arr, leftpt, rightpt):
    global countcompare
    pivot= arr[leftpt]
    i= leftpt+1
    countcompare+=len(arr[leftpt+1:rightpt+1])
    
    #for j in range(leftpt+1,len(arr[leftpt+1:rightpt+1])+1):
    for count,_ in enumerate(arr[leftpt+1:rightpt+1]):

        j=count+leftpt+1
        if arr[j] < pivot:
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
    arr[leftpt],arr[i-1]=arr[i-1],arr[leftpt]

    return i-1



def quicksort(arr,leftpt,rightpt):
    if leftpt>=rightpt:
        return 0 

    else:
        
        i = choosepivot(arr,leftpt,rightpt)
        arr[leftpt],arr[i]=arr[i],arr[leftpt]



        j = partition(arr,leftpt,rightpt)
        quicksort(arr,leftpt,j-1)
        quicksort(arr,j+1,rightpt)



if __name__=="__main__":


    f = open("Quicksort.txt","r")
    f=f.read()
    str_to_int= lambda lst: ([int(num) for num in lst])
    arr=array("i", str_to_int(re.findall(r"[-+]?\d*\.\d+|\d+", f)))

    #arr=array("i",[3,8,2,5,1,4,7,6])
    #arr=array("i",list(range(100)))
    #arr.reverse()
    quicksort(arr,0,len(arr)-1)
    print("countcomparetot ",countcompare)
    #print(*arr,sep="\n")
