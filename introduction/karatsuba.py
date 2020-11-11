from time import time
import ipdb
from math import ceil,floor

#def get_half(num:str)->str:
#    return num[:int(len(num)/2)] , num[int(len(num)/2):]

def karatsuba(x:int,y:int):
    
    if x==0 or y==0:
        #print(locals())
        return 0
    numx,numy=str(x),str(y)
    get_n=lambda numx,numy:(len(numx),"0"*(len(numx)-len(numy))+numy) 
    if len(numx)>=len(numy):
        #n=len(numx)
        n,numy=get_n(numx,numy)
    elif len(numx)<len(numy) :
        #n=len(numy)
        n,numx=get_n(numy,numx)
    
    if not n%2==0 and not n==1:
        numx="0"+numx
        numy="0"+numy
        n=len(numx)


    assert len(numx)==len(numy)
    
        
    #n=len(numx)

    if n==1:
        #print(locals())
        result = x*y
        #print(f"result {result}") 
        return result

    else:
        #print(locals())
        #numx=str(x)
        #numy=str(y)
        
        get_half=lambda num:((num[:int(len(num)/2)] , num[int(len(num)/2):]) 
                                if not len(num)==1 else ('0', num))
        #get_half=lambda num:((num[:ceil(len(num)/2)] , num[ceil(len(num)/2):]) 
        #                        if not len(num)==1 else ('0', num))

        a,b = get_half(numx) 
        c,d = get_half(numy)
        
        #ipdb.set_trace()
        #print(locals())
        a,b,c,d = int(a),int(b),int(c),int(d)
        #try:
        #    a,b,c,d = int(a),int(b),int(c),int(d)
        #except:
        #    ipdb.set_trace()            
        p, q = a+b, c+d
        #print("="*20)
        #print(locals())
        ac, bd, pq = karatsuba(a,c), karatsuba(b,d), karatsuba(p,q)
        
        adbc = pq-ac-bd
        #print(f"n {n}") 
        #breakpoint()
        #ipdb.set_trace()
        #print(locals())
        
        #if not n%2==0:
        #    print(f"nvalue {n}")
        #    result=10**n * ac + 10**(ceil(n/2)) * adbc + bd
        #else:
        #    result=10**n * ac + 10**(int(n/2)) * adbc + bd
        result=10**n * ac + 10**(int(n/2)) * adbc + bd

        #print(f"result {result}")
        return result  

x=3141592653589793238462643383279502884197169399375105820974944592
y=2718281828459045235360287471352662497757247093699959574966967627

#x=108
#y=110
start=time()
result=karatsuba(x,y)
end=time()
#assert result== x*y
print(f"karatsuba product of {x} and {y} is {result}")
print("product from python ",x*y)
print("difference ",result-x*y)
print(f"time required {end-start}")
    
