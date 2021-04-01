from linkedlist import Node,LinkedList
import re,sys,shutil
import random
from array import array


def count_lines(afile,size=65536):
    while True:
        b = afile.read(size)
        if not b: break
        yield b


def random_line(afile):
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
#<<<<<<< HEAD

                ll.remove_node(targetnode_data=other)
                ll.add_first(node=Node(head))
#        else:
#            if elem.data==other:
#                ll.add_after(targetnode=prevnode.data,newnode=Node(head))
#=======
        else:
            if elem.data==other:
                ll.add_after(targetnode=other,newnode=Node(head))
#>>>>>>> 1c70fb6
                ll.remove_node(targetnode_data=other)
            prevnode=elem

    #print(f"linkedlist after removal is {ll}")
#<<<<<<< HEAD
    #return ll

def recurse():
    basefile="test_case_base.txt"
    resultfile="test_case_result.txt"

    with open(basefile, "r") as f:
        total_linum=sum(bl.count("\n") for bl in count_lines(f))
    if total_linum>2:
        with open(basefile, "r") as f:
            randline = random_line(f)
            #print(f"randline {randline}")

        
        randlinelist=randline.split()
        
        head, other=randlinelist[0],random.choice(randlinelist[1:])
        #print(f"random choice head {head} other {other}")    
        #ll1 = LinkedList(nodes=randlinelist)

        #ll1 = LinkedList(nodes="1 2 3 4".split())
        #head,other ="2","3"

        #contract(ll1,head,other)


        #fbase = open("test_case_base.txt","r")
        #gline=(line for line in fbase if not line==randline)
        
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
                    if not ll.head.data==head:
                        fresult.write(repr(ll)+"\n")
                    else:
                        temp.append(repr(ll))
        
        
        fresult =open(resultfile,"a")

        if len(temp)==2:
            print(temp[0],temp[1].strip(head),sep="",file=fresult)
        elif len(temp)==1:
            print(temp[0],file=fresult)

        fresult.close()

        shutil.copyfile(resultfile,basefile)

        #fbase.close()
        recurse()

    else:
        #print(f"linum={total_linum}")
        return

    #else:

        
#=======
#>>>>>>> 1c70fb6



if __name__=="__main__":
    
    iteration_num=100
    i=0
    temp=array('I',[])
    while(i<100):
        recurse()
        shutil.copy("test_case_base_orig.txt","test_case_base.txt")    
        resultfile="test_case_result.txt"
        cutnum =len(open(resultfile).readline().split()[1:])
        temp.append(cutnum)
        print(f"cutnum {cutnum}")
        i+=1

    print(f"minimum cut={min(temp)}")



    










#<<<<<<< HEAD
#=======
#    with open("test_case_base.txt", "r") as f:
#        randline = random_line(f)
#        print(f"randline {randline}")
#
#    #f1 = open("test_case_base.txt","r")
#    #gline=(line for line in f1 if not line==randline)
#
#    #with open("test_case_result.txt","w") as f2:
#    #    for line in gline:
#    #        print(f"gline {line}")
#    #        f2.write(line)
#    #f1.close()
#    
#    randlinelist=randline.split()
#    
#    #head, other=randlinelist[0],random.choice(randlinelist[1:])
#    #print(f"random choice head {head} other {other}")    
#    #ll1 = LinkedList(nodes=randlinelist)
#
#    ll1 = LinkedList(nodes="8 6 6 7".split())
#    head,other ="7","6"
#
#    contract(ll1,head,other)
#
#    
#
#    
#
#
#
#
#
#
#
#
#
#
#>>>>>>> 1c70fb6


