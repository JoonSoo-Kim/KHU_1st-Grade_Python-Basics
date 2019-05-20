def decideNumber(inputNum):
    if inputNum%2==0 :
        resultStr='Even Number'
        return resultStr
    elif inputNum%2==1 :
        resultStr='Odd Number'
        return resultStr
    else :
        resultStr='정수를 입력해주세요'
        return resultStr

inputNum = int(input("숫자를 입력해주세요."))
print(decideNumber(inputNum))