tableList=[]
nNum=int(input("N : "))
for i in range(1,nNum+1):
    for j in range(i,nNum+i):
        tableList.append(j)
    for k in range(nNum):
        tableList[i]='-'
        if i < k:
            tableList[k]='+'
    if i%2==0 and i>3:
        for s in range(1,nNum+1):
            if s==1:
                continue
            elif (s/2)+1 == 2.5:
                tableList[s-1]='*'
    print(tableList)
    tableList=[]