import mmap


def mmap_io(filename):
    with open(filename, mode="r+", encoding="utf8") as file_obj:
        with mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_WRITE) as mmap_obj:
            #print(mmap_obj[10:16])
            mmap_obj[10:16]=b"python"
            mmap_obj.flush()



if __name__=="__main__":
    filename="test_case1.txt" 
    mmap_io(filename)

