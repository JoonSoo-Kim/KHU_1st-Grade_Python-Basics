name = input("Hello. what's your name?")
age = int(input("How old are you?"))
nowYear = int(input("Years of this (ex : 2019) : "))

print('Your name is', name)
print(name, 'is', age, 'years old')
print(name, 'is', age+(2039-nowYear), 'years old in 2039')
print(name, 'is', age+(2099-nowYear), 'years old in 2099')