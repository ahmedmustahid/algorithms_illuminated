from linkedlist import Node,LinkedList
import re,sys,shutil
import random


def count_lines(afile,size=65536):
    while True:
        b = afile.read(size)
        if not b: break
        yield b

    with open("test_case_base.txt", "r") as f:
        print(sum(bl.count("\n") for bl in count_lines(f)))

def random_line(afile):
    line = next(afile)
    flag = re.match("\n+",line)
    print(f"is newline? {flag}")
    while flag is not None:
        print(f"line {line}")
        line = re.sub("\n+","",line)
        flag = re.match("\n+",line)
        print(f"flag is {flag}")

    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            #print(f"inside randrange {num}")
            continue
        if not re.match(r"\n+",aline):
            line = aline
            #print(f"num {num} aline {aline}")
    return line
    
def contract(ll: LinkedList,head,other):
    print(f"linkedlist is {ll}")
    
    prevnode=ll.head
    for elem in ll:

        if ll.head.data==head:
            if elem.data==other:
                ll.remove_node(targetnode_data=other)
        elif ll.head.data==other:
            if elem.data==head:
                ll.remove_node(targetnode_data=head)
        else:
            if elem.data==other:
                ll.remove_node(targetnode_data=other)
                ll.add_after(targetnode=prevnode.data,newnode=Node(head))
            prevnode=elem

    print(f"linkedlist after removal is {ll}")



if __name__=="__main__":

    with open("test_case_base.txt", "r") as f:
        randline = random_line(f)
        print(f"randline {randline}")

    #f1 = open("test_case_base.txt","r")
    #gline=(line for line in f1 if not line==randline)

    #with open("test_case_result.txt","w") as f2:
    #    for line in gline:
    #        print(f"gline {line}")
    #        f2.write(line)
    #f1.close()
    
    randlinelist=randline.split()
    
    head, other=randlinelist[0],random.choice(randlinelist[1:])
    print(f"random choice head {head} other {other}")    
    ll1 = LinkedList(nodes=randlinelist)

    #ll1 = LinkedList(nodes="1 2 3 4".split())
    #head,other ="2","3"

    contract(ll1,head,other)

    

    












