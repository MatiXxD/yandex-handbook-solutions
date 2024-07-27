num1 = int(input())
num2 = int(input())

nok = num1 * num2
n = num2
while n < num1 * num2:
    if n % num1 == 0 and n % num2 == 0:
        nok = n
        break
    n += num2
print(nok)
