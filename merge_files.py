import os

f1 = open("PlasStopLi.txt","r")
lines1 = f1.readlines()
result = []
f2 = open("PlasStopLi2.txt","r")
lines2 = f2.readlines()
print("hola" + lines2)
result2 = []
mf = open("SumStopLi.txt","w+")
for i in lines1:
    result.append(i.split(' ')[1])
    print [i.split(' ')[1]

#for j in lines2:
#    result2.append(i.split(' ')[1])

f1.close()
f2.close()
mf.close()
