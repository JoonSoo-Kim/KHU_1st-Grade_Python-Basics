leaf=input("enter your code for leaf : ")
column=input("enter your code for column : ")

for i in range(8):
    print(((2*i-1)*leaf).center(13))
for i in range(3):
    print((3*column).center(13))