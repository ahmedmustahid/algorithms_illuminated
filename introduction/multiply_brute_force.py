from time import time
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("x", help="one of the two multiples",type=int)
parser.add_argument("y", help="one of the two multiples",type=int)
args = parser.parse_args()
#print(args.x * args.y)

x,y=str(args.x),str(args.y)
getnums= lambda x,y:(x,"0"*(len(x)-len(y))+y)

if len(x)>len(y):
    x,y=getnums(x,y)
elif len(x)<len(y):
    y,x=getnums(y,x)
else:
    pass
start=time()
prod=0
for i,digx in enumerate(x[::-1]):
    for j,digy in enumerate(y[::-1]):
        prod+=10**(i+j)*(int(digx)*int(digy))
end=time()
print(f"{int(x)}*{int(y)} is {prod}")
print(f"python product is {int(x)*int(y)}")
print(f"time required {end-start}")
    
