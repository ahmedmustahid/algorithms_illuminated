from array import array


def merge(arr1: array, arr2: array)->array:

    n = len(arr1)+len(arr2)
    arr_fin= array("i",[])

    i,j=0,0
    
    for k in range(n):
        #checking if one of the iterators is at the end
        if i==int(len(arr1)):
            #arr_fin.insert(k,arr2[j])
            arr_fin.extend(arr2[j:])
            return arr_fin
        elif j==int(len(arr2)):
            #arr_fin.insert(k,arr1[i])
            arr_fin.extend(arr1[i:])
            return arr_fin
       
        if arr1[i] < arr2[j]:
            arr_fin.insert(k,arr1[i])
            i+=1
            print("inside arr1\n ",locals())
        else:
            arr_fin.insert(k,arr2[j])
            j+=1
            print("inside arr2\n ",locals())

    return arr_fin

def mergesort(arr_in: array)->array:

    #n=len(arr)
    if len(arr_in)==1:
        return arr_in

    else:
        arr_inleft, arr_inright = mergesort(arr_in[:int(len(arr_in)/2)]), mergesort(arr_in[int(len(arr_in)/2):])
        return merge(arr_inleft,arr_inright)


if __name__=="__main__":

    #arr1=array("i",[1,4,5,8])
    #arr2=array("i",[2,3,6,7])

    #print(merge(arr1,arr2))

    arr_in=array("i",[5,4,1,8,7,2,6,3])
    print(mergesort(arr_in))
