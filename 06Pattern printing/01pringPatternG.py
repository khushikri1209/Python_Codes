# Python program to print pattern G
def Pattern(line):
    pat=""
    for i in range(0,line):    
        for j in range(0,line):     
            if ((j == 1 and i != 0 and i != line-1) or ((i == 0 or
                i == line-1) and j > 1 and j < line-2) or (i == ((line-1)/2)
                and j > line-5 and j < line-1) or (j == line-2 and
                i != 0 and i != line-1 and i >=((line-1)/2))):  
                pat=pat+"*"   
            else:      
                pat=pat+" "   
        pat=pat+"\n"   
    return pat
 
# Driver Code
line = 7
print(Pattern(line))