size = int(input())
width = int(input())

row_len = (width + 1) * size - 1
for i in range(1, size + 1): 
    for j in range(1, size + 1):
        end_with = "|"
        if j == size:
            end_with = "\n"
        print((f"{i*j}" + (" " if width % 2 else "")).center(width), end=end_with)
    if i != size:
        print("-" * row_len)
