num1 = int(input())
num2 = int(input())

mcd = 1
min_num = min(num1, num2)
for d in range(1, min_num // 2 + 1):
    if num1 % d == 0 and num2 % d == 0:
        mcd = d
print(mcd)
