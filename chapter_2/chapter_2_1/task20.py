n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

n1 = (m - k2) * n / (k1 - k2)
n2 = (k1 - m) * n / (k1 - k2)
print(int(n1), int(n2))
