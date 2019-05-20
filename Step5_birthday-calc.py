codeNum = int(input("생년월일 8자리 : "))
yearNum = codeNum//10000
monthNum = codeNum//100 - yearNum*100
dayNum = codeNum%100

print("당신의 생일은", yearNum,"년",monthNum,"월",dayNum,"일 입니다.")
