from array import array


def merge(arr1: array, arr2: array)->array:

    n = len(arr1)+len(arr2)
    arr_fin= array("i",[])

    i,j=0,0
    
    for k in range(n):
        #checking if one of the iterators is at the end
        if i==int(len(arr1)):
            arr_fin.insert(k,arr2[j])
            return arr_fin
        elif j==int(len(arr2)):
            arr_fin.insert(k,arr1[i])
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


if __name__=="__main__":

    arr1=array("i",[1,4,5,8])
    arr2=array("i",[2,3,6,7])

    print(merge(arr1,arr2))
