n = int(input())
m = int(input())
t = int(input())

mins = 60 * n + m + t
hours = mins // 60
mins -= 60 * hours
hours %= 24

print(f"{hours:0>2}:{mins:0>2}")
