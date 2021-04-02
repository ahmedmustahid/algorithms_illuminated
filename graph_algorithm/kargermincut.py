from linkedlist import Node,LinkedList
import re,sys,shutil
import random
from array import array

hitnum=0
def count_lines(afile,size=65536):
    while True:
        b = afile.read(size)
        if not b: break
        yield b


def random_line(afile):
    global seednum
    seednum+=1
    random.seed(seednum)
    line = next(afile)
    flag = re.match("\n+",line)
    #print(f"is newline? {flag}")
    while flag is not None:
        #print(f"line {line}")
        line = re.sub("\n+","",line)
        flag = re.match("\n+",line)
        #print(f"flag is {flag}")

    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            #print(f"inside randrange {num}")
            continue
        if not re.match(r"\n+",aline):
            line = aline
            #print(f"num {num} aline {aline}")
    return line
    
def contract(ll: LinkedList,head,other):
    #print(f"linkedlist is {ll}")
    
    prevnode=ll.head
    for elem in ll:

        if ll.head.data==head:
            if elem.data==other:
                ll.remove_node(targetnode_data=other)
        elif ll.head.data==other:
            if elem.data==head:
                ll.remove_node(targetnode_data=head)

                ll.remove_node(targetnode_data=other)
                ll.add_first(node=Node(head))
        else:
            if elem.data==other:
                ll.add_after(targetnode=other,newnode=Node(head))
                ll.remove_node(targetnode_data=other)
            prevnode=elem

def recurse():
    global seednum    
    global hitnum
    hitnum+=1
    seednum+=1
    random.seed(seednum)
    print(f"start seednumfin {seednum}")
    basefile="test_case_base.txt"
    resultfile="test_case_result.txt"

    with open(basefile, "r") as f:
        total_linum=sum(bl.count("\n") for bl in count_lines(f))
    if total_linum>2:
        with open(basefile, "r") as f:
            randline = random_line(f)
            print(f"randline {randline}")

        
        randlinelist=randline.split()
        
        head, other=randlinelist[0],random.choice(randlinelist[1:])
        print(f"head {head} other {other}") 
        temp=[]
        with open(basefile,"r") as fbase:
            with open(resultfile,"w") as fresult:
                for line in fbase:
                    if re.match('\n+',line):
                        continue
                    if len(line.split())==1:
                        continue
                    ll = LinkedList(nodes=line.split())
                    contract(ll=ll,head=head,other=other)
                    
                    #if len(ll)>1:
                    #if ll.head.next is not None:
                    if not ll.head.data==head:
                        print(f"hitnum {hitnum}")
                        print(ll)
                        fresult.write(repr(ll)+"\n")
                    else:
                        #print(ll)
                        if ll.head.next is not None:
                            temp.append(repr(ll))
        
        
        fresult =open(resultfile,"a")

        if len(temp)==2:
            string1= temp[0]
            string2=re.sub(rf'\b{head}\b','',temp[1])
            print(string1,string2,sep="",file=fresult)
            print(string1,string2,sep="")
            print("end\n")
        elif len(temp)==1:
            print(temp[0],file=fresult)
            print(f"temp0 {temp[0]}")
            print("end\n")

        fresult.close()

        shutil.copyfile(resultfile,basefile)

        #fbase.close()
        recurse()

    else:
        #print(f"linum={total_linum}")
        return


seednum=0


if __name__=="__main__":
    #global seednum    
    iteration_num=100
    i=0
    temp=array('I',[])
    #while(i<6):
    while(i<int(sys.argv[1])):
        print(f"iteration_num {i}")
        recurse()
        shutil.copy("test_case_base_orig.txt","test_case_base.txt")    
        resultfile="test_case_result.txt"
        cutnum =len(open(resultfile).readline().split()[1:])
        temp.append(cutnum)
        if cutnum==1:
            break
        print(f"cutnum {cutnum}")
        i+=1

    print(f"minimum cut={min(temp)}")
