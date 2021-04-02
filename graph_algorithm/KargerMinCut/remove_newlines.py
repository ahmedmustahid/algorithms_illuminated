import re

rows=[]
f2=open("test_case2.txt","w")
with open("test_case1.txt","r") as lines:
    for line in lines:
        print("before replace ")
        print(line)
        line = re.sub("[\s\n]+","",line)
        print("after replace")
    
        print(line)
        rows.append(line)

for row in rows:
    f2.write(row+"\n")

f2.close()

        

