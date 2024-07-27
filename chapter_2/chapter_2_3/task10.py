x = 0
y = 0

direction = input()
while direction != "СТОП":
    repeat = int(input())
    if direction == "СЕВЕР":
        y += repeat
    elif direction == "ЮГ":
        y -= repeat
    elif direction == "ЗАПАД":
        x -= repeat
    elif direction == "ВОСТОК":
        x += repeat
    direction = input()

print(y)
print(x)
