import sys
import re
import numpy as np
filename = f"G:\gam3a\System Programming\Lab\\absolute loader\\hte_4.txt"
array = []
start_ = 0
xline = ""
xstring = ""
addr_line = ""
length = 0
is_xs = False
with open(filename) as f:
    for line in f:
        # try:
        line = line.replace('\n', '').split(".")
        if(line[0] == "H"):
            start_ = line[2] #start code in header(H)
        elif(line[0] == "T"):
            try:
                if(length != str(line[1]).lower and length != 0): #check if length not equal start code in Text(T)
                    xs = abs(int(line[1], 16)-length)*2 #the number of x`s(current start code in Text(T) - length(old start code in Text(T)+the Length of old Text(T)))
                    is_xs = True
            except:
                print()

            length = int(line[1], 16)+int(line[2], 16) #length equation = (start code +length)in Text(T)
            addr_line = line[3:None]#address line start from index 3 to the end(None=To end)
            if(is_xs):#is there is x in address line
                is_xs=False
                for i in range(0, xs):#adding the xs value
                    xstring += "x"
            for i in range(0, addr_line.__len__()):#make all thing in one line(el trickaya el gamda gedn)
                xstring += addr_line[i]
            # if(addr_line!=""): #break program in first instruction
            #     break

element = 0
column = 0
text = ""
for i in range(0, xstring.__len__()):#split the xstring to 4 elements(length=8) in the row seperated by (.)
    if(element == 8):
        text += "."
        element = 0
        column += 1
        if(column == 4):#make 4*4 elements in 1 column
            text += " "
            column = 0
    text += xstring[i]
    element += 1
array.append(list(text.split(".")))


real_array = [[[start_[2:]]]]
index = 0
column = 0
for i in range(0, array[0].__len__()):#put the memoryaddress(start_) to array
    if(column == 4):
        index += 1
        start_ = hex(int(start_,16)+16)[2:]#get start from Header(H) and adding to 16
        real_array.append([[start_]])
        column = 0
    real_array[index].append([array[0][i]])#to append element to current row
    column += 1

for i in range(0, real_array.__len__()):#print ALL
    print(real_array[i])

file1 = open("MyFile.txt","a")
for ex in real_array:
    
    file1.write(str(ex))
file1.close()


#coded with 💖 by marwaneldesouki