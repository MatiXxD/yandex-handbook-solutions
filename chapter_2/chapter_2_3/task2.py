str_count = 0
txt = input()
while txt != "Приехали!":
    if "зайка" in txt:
        str_count += 1
    txt = input()
print(str_count)
