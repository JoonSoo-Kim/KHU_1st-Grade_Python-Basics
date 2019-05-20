import random

print("숫자를 하나 생각해주세요. (1~100)")
Limit_i=0
Limit_f=101
while True:
    guessNum=random.randrange(Limit_i,Limit_f)
    print("컴퓨터가 예상한 숫자 :", guessNum)
    answer=int(input("이 숫자보다 크면 2, 같으면 1, 작으면 0을 입력해주세요. : "))
    if answer==2:
        Limit_i=guessNum+1
        continue
    elif answer==1:
        break
    elif answer==0:
        Limit_f=guessNum
 

