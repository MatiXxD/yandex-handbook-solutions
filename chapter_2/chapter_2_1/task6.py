name = input()
price = int(input())
weight = int(input())
paid = int(input())

total_price = weight * price

print("Чек")
print(f"{name} - {weight}кг - {price}руб/кг")
print(f"Итого: {total_price}руб")
print(f"Внесено: {paid}руб")
print(f"Сдача: {paid-total_price}руб")
