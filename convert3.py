# 2 -> 10進数へ
n = '10010'
result = 0
# i = 0

# while i < 5: <- 桁数をとりたい　-> for文が使える
#     int(n[i]) = 2 ** (5-i)
#     result = int(n[i]) + result
for i in range(len(n)):
    result += int(n[i]) * (2 ** (len(n) - i - 1))

print(result)

a = 0b10010
print(a)