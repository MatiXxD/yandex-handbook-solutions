a = float(input())
b = float(input())
c = float(input())

if a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
    print("100%")
elif a * a > b * b + c * c or b * b > a * a + c * c or c * c > a * a + b * b:
    print("велика")
else:
    print("крайне мала")
