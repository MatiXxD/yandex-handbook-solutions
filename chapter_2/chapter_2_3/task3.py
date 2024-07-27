a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i != b:
        print(i, end=" ")
    else:
        print(i)
