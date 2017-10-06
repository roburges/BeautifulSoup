import re

myData=open("actual.txt")
mylst = []
mynewlst =[]
for line in myData:
    #line=line.rstrip()
    mystuff=re.findall('[0-9]+',line)
    for number in mystuff:
        mylst.append(int(number))
myanswer=sum(mylst)
print(myanswer) 
