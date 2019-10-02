#coding: utf8
#!/usr/bin/python
import os
max_num = 0
def get_max_person(n):
    max_num = len(bin(n-1)[2:])
    return max_num

def get_bin(n):
    set_bin = (bin(n-1)[2:].zfill(max_num))
    #print(set_bin)
    index = 1
    try_set =""
    for i in set_bin[0:]:
        if int(i) == 1 :
            #print("编号%d试喝%d号药液"% (index, n))
            try_set = try_set + str(index)+","
        
        index = index + 1
    if len(try_set) == 0:
        return set_bin, None
    else:
        return  set_bin, try_set
            


if __name__ == "__main__":
    max_num = get_max_person(64)
    print("最少需要%d人去试毒，3天后可以知道结果。"% max_num)
    print("试毒步骤把%d人，排成一排，分别编号: %s" %(max_num, range(1,max_num+1)))
    print("药瓶编号, 药瓶二进制, 需要喝药的编号")
    for i in range(0,64):
        #print i
        seq_bin, try_set = get_bin(int(i+1))
        print(i+1, seq_bin, try_set)
        #print("--------------------")
