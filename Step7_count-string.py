def calcCharacterFromString(calcStr,want_to_count):
    return calcStr.count(want_to_count)

inputStrs = input("문자열을 넣어주세요 : ")
inputStr = input("세고 싶은 문자를 하나 넣어주세요 : ")
print(calcCharacterFromString(inputStrs,inputStr))