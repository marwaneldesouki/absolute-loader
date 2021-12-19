import sys
import re
filename = f"G:\gam3a\System Programming\Lab\\absolute loader\\hte.txt"
array=[]
start_=0
xline=""
xstring=""
with open(filename) as f:
    for line in f:
        # try:
            line = line.replace('\n','').split(".")
            if(line[0]=="H"):
                start_ = line[2]
                print(start_)
            elif(line[0]=="T"):
                line_ = line[3:None]
                x = int(int(line[2],16)/3)
                xline = str(start_)
                for i in range(0,x):
                    xline += line_[i]
                    
                for i in range(0, len(xline),2):
                    xstring+=xline[i : i + 2]+","
                xstring = xstring[:-1]
                xstring = xstring.split(',')
                xstring.insert(0,start_)
                array.append(xstring)
                xstring=""
                xline=""
                start_=  int(start_)+10
print(array)
    # print(array[1])
            
        # except Exception as ex :
        #     print(ex)