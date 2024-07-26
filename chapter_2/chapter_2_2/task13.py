num1 = input()
num2 = input()
num3 = input()

digit1 = num1[0]
digit2 = num1[1] 

if digit1 in num2 and digit1 in num3:
    print(digit1)
else:
    print(digit2)
