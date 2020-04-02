f1=open("PlasStopLi.txt","r")
lines=f1.readlines()
result=[]
mf = open("SumStopLi.txt","w+")

for i in lines:
    if not i=='':
        result.append(i.strip().replace('  ',' ').split(' ')[1])

f1.close()

f2 = open("PlasStopLi2.txt","r")
lines=f2.readlines()
result2=[]

for j in lines:
    if not j=='':
        result2.append(j.strip().replace('  ',' ').split(' ')[1])

f2.close()
tresult = []

for i in range(49):
    try:
        if not i=='':
            tresult[i]=float(result[i])+float(result2[i])
    except:
        print("result 1: " + result[i] + " result 2: " + result2[i])

for i in range(0,5.1,0.1):
    mf.write(str(i) + '\t' + str(tresult[i]))

mf.close()
