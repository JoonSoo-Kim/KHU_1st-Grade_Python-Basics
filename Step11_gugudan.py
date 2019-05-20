gugulist=[]
for i in range(1,10):
    for j in range(1,10):
        gugulist.append(str(i*j).center(5))
    print(gugulist)
    gugulist=[]