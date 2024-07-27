total_price = 0
price = float(input())
while price != 0:
    if price >= 500:
        price *= 0.9
    total_price += price
    price = float(input())
print(total_price)
