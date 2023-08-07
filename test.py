# それでは、A と B をそれぞれ 1 以上 512 以下の整数としたときに、A ÷ B の余りを全て足した値を求めてください。
remainder_total = 0

for i in range(1, 513):
    for j in range(1, 513):
        remainder = i % j
        remainder_total += remainder

print(remainder_total)

# 100001110
test = 31622 ** 2
print(test)

# 3.1412
N_total = 0

for i in range(1, 1275):
    j = 2*i - 1
    down = (2*j - 1) * (2*j + 1)
    N = 8 / down
    N_total += N

print(N_total)