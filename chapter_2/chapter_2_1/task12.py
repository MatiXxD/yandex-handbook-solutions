num1 = int(input())
num2 = int(input())

num1 = f"{num1:0>3}"
num2 = f"{num2:0>3}"

print(
    f"{(int(num1[0]) + int(num2[0])) % 10}{(int(num1[1]) + int(num2[1])) % 10}{(int(num1[2]) + int(num2[2])) % 10}"
)
