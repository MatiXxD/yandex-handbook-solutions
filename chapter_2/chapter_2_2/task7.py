num = int(input())

if num % 10 == num // 1000 and (num % 1000) // 100 == (num // 10) % 10:
    print("YES")
else:
    print("NO")
