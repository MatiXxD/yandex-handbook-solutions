num = int(input())

is_simple = True
n = 2
while n * n <= num:
    if num % n == 0:
        is_simple = False
    n += 1

if is_simple and num >= 2:
    print("YES")
else:
    print("NO")
