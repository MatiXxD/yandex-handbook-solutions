def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    return max(a, b)


n = int(input())

cur_nod = int(input())
for _ in range(n - 1):
    num = int(input())
    cur_nod = nod(cur_nod, num)

print(cur_nod)
