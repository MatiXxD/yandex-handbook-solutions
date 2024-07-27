a = int(input())
b = int(input())
step = -1 if b < a else 1

for i in range(a, b + step, step):
    if i != b:
        print(i, end=" ")
    else:
        print(i)
