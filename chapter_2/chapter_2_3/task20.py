wrong_hash_pos = -1
n = int(input())

prv_hash = 0
for i in range(n):
    b = int(input())
    hn, rn, mn = b % 256, b // 256 % 256, b // (256 * 256)
    h = (37 * (mn + rn + prv_hash)) % 256
    if hn != h or hn >= 100:
        wrong_hash_pos = i
        break 
    prv_hash = hn

print(wrong_hash_pos)
