

def get_half(num:str)->str:
    return num[:int(len(num)/2)] , num[int(len(num)/2):]

def karatsuba(x:int,y:int):

    numx=str(x) 
    n=len(numx)

    if n==1:
        return x*y

    else:
        numx=str(x)
        numy=str(y)

        a,b = get_half(numx) 
        c,d = get_half(numy)
        
        a,b,c,d = int(a),int(b),int(c),int(d)
        p, q = a+b, c+d
        ac, bd, pq = karatsuba(a,c), karatsuba(b,d), karatsuba(p,q)
        
        adbc = pq-ac-bd
        #print(f"n {n}") 
        breakpoint()
        
        return 10**n * ac + 10**(int(n/2)) * adbc + bd


#x=3141592653589793238462643383279502884197169399375105820974944592
#y=2718281828459045235360287471352662497757247093699959574966967627

x=1000
y=9999

result=karatsuba(x,y)
#assert result== x*y
print(result)
print(x*y)
    
