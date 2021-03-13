import random
import mmap
import re,os,shutil


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
    
    #filename="test_case1.txt" 
    filename="KargerMinCut_challenge_case.txt" 
    line_count =sum(line.count('\n') for line in open(filename,"r"))

    while line_count>2:
        randline = random_line(filename)
        print(f"randline {randline}")
        find_and_delete(filename,randline)
        line_count =sum(line.count('\n') for line in open(filename,"r"))
        print(f"line_count {line_count}")
    else:
        print(f"line_count {line_count} is minimum")






