def decideLarger(numA, numB) :
    if numA > numB :
        return numA
    elif numA < numB :
        return numB
    else :
        return '두 숫자가 동일합니다'

inputNumA, inputNumB = input("두 개의 숫자를 띄워서 입력해주세요.").split()
print(decideLarger(inputNumA, inputNumB))