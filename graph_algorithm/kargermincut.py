from linkedlist import Node,LinkedList
import re,sys,shutil
import random


def count_lines(afile,size=65536):
    while True:
        b = afile.read(size)
        if not b: break
        yield b

with open("test_case2.txt", "r") as f:
    print(sum(bl.count("\n") for bl in count_lines(f)))
sys.exit()

def random_line(afile):
    line = next(afile)
    flag = re.match("\n+",line)
    print(f"flag is {flag}")
    while flag is not None:
        print(f"line {line}")
        line = re.sub("\n+","",line)
        flag = re.match("\n+",line)
        print(f"flag is {flag}")

    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            print(f"inside randrange {num}")
            continue
        if not re.match(r"\n+",aline):
            line = aline
            print(f"num {num} aline {aline}")
    return line

#def getline(afile,randline):
#    for line in afile:
#        yield line


if __name__=="__main__":

    with open("test_case1.txt", "r") as f:
        randline = random_line(f)
        print(f"randline {randline}")

    with open("test_case1.txt", "r") as f:
        lines = f.readlines()
        total_lines=sum(bl.count("\n") for bl in lines)
    #with open("test_case1.txt", "r") as f:
    #    lines = f.readlines()
    #    #line_count=sum()
    f1 = open("test_case1.txt","r")
    gline=(line for line in f1 if not line==randline)

    with open("test_case2.txt","w") as f2:
        for line in gline:
            print(f"gline {line}")
            f2.write(line)

    f1.close()

    sys.exit()
    with open("test_case1.txt", "r+") as lines:
        for line in lines:
            line = re.sub(r"\n+","\n",line).strip("\n")
            randline=randline.strip("\n")
            if line == randline:
                line.strip(line)
                print(f"line {line} is stripped")
                #line=line+"\n"
                lines.write(line)

    print(f"total_lines {total_lines}")
    sys.exit()

    with open("test_case1.txt", "r") as f:
        total_lines=sum(bl.count("\n") for bl in count_lines(f))
        #print()

    if total_lines>2:
        with open("test_case1.txt", "w") as f:
            for line in lines:
                line = re.sub(r"\n+","\n",line).strip("\n")
                randline=randline.strip("\n")
                if line != randline:
                    print(f"line {line}")
                    line=line+"\n"
                    f.write(line)

    #sys.exit()

    f = open("test_case1.txt",mode="r")

    l = random_line(f)
    print(f"random line {l.split()}")

    with open("test_case1.txt","r+") as fs:
        for c in fs:
            if not c.strip("\n")==l:
                print(c)
                fs.write(c)

    with open("test_case1.txt","r") as lines:
        for line in lines:
            print(line)

    #ll1=LinkedList(l.split())
    #print(ll1)


