import random
import mmap
import re,os,shutil,sys
from linkedlist import LinkedList,Node

def find_and_delete(filename,randline):
    

    with open(filename, "r", encoding="utf-8") as orig_file_obj:
        with open("tmp.txt", "w", encoding="utf-8") as new_file_obj:
            #orig_text = orig_file_obj.read()
            for line in orig_file_obj:
                regrand=r""+randline+"[\n]?"
                if not bool(re.findall(regrand,line)):
                    new_file_obj.write(line)

            #randline=randline+"\n"
            #new_text = orig_text.replace(randline, "")
            #new_file_obj.write(new_text)

    shutil.copyfile("tmp.txt", filename)
    os.remove("tmp.txt")



def mmap_io(filename,randline):
    with open(filename, mode="r+", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_obj:
            text = mmap_obj.read()
            randline=randline.encode('utf_8')
            new_text = text.replace(randline, b"")
            
            #print(f"new txt {new_text}")
            mmap_obj[:]=new_text
            mmap_obj.flush()
            #while True:
            #    line = mmap_obj.readline()
            #    print(line)
            #    if not line:
            #        break




def random_line(filename):
    with open(filename,"r") as afile:
        line = next(afile)
        for num, aline in enumerate(afile, 2):
            if random.randrange(num):
                #print(f"inside randrange {num}")
                continue
            if not re.match(r"\n+",aline):
                line = re.sub(r"\n+","",string=aline)
                #print(f"num {num} aline {aline}")
    return line


if __name__=="__main__":
    
    filename="test_case1.txt" 
    #filename="KargerMinCut_challenge_case.txt" 
    line_count =sum(line.count('\n') for line in open(filename,"r"))
    
    while line_count>=2:
        randline = random_line(filename)
        randline=randline.strip("/n").split()
        
        head1=randline[0]
        node1=random.choice(randline)
        while node1==head1:
            node1=random.choice(randline)

        print(f"head1 {head1} node1 {node1}")
        temp=[]
        with open(filename,"r") as f:
            with open("tmp.txt", "w", encoding="utf-8") as new_file_obj:
                for line in f:
                    line=line.strip("/n").split()
                    
                    ll= LinkedList(line)
                    if ll.head.data==node1:
                        ll.remove_node(ll.head.data)
                        ll.add_first(Node(head1))
                    #print("change head") 
                    #print(ll)
                    prevnode=ll.head
                    for i,node in enumerate(ll):
                        #if i==0:
                        #    continue
                        if i>0 and node.data==node1 and node.data!=ll.head.data:
                            ll.remove_node(node.data)         
                            ll.add_after(prevnode.data,Node(head1))
                            if ll[i].data==ll.head.data:
                                prevnode.next = ll[i].next
                        elif i>0 and node.data==ll.head.data:
                            prevnode.next=node.next
                        prevnode=node
                        
                    if ll[0].data==head1:
                        temp.append(ll)
                    else:
                        print(*ll,file=new_file_obj)
                print("in temp list")
                for t in temp:
                    print(t)
                ll1,ll2=temp[0],temp[1]
                m=[]
                for i,l1 in enumerate(ll1):
                    m.append(l1.data)
                    for j,l2 in enumerate(ll2):
                        if i==j and i>0 and j>0:
                            m.append(l2.data)

                print(' '.join(m),file=new_file_obj)
                print(m)
        
        
        shutil.copy('tmp.txt',filename)
        os.remove('tmp.txt')
        line_count =sum(line.count('\n') for line in open(filename,"r"))

    sys.exit()


    while line_count>2:
        randline = random_line(filename)
        print(f"randline {randline}")
        

        find_and_delete(filename,randline)
        line_count =sum(line.count('\n') for line in open(filename,"r"))
        print(f"line_count {line_count}")
    else:
        print(f"line_count {line_count} is minimum")






