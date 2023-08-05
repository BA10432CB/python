# 10進数から2進数への変換
n = 18
result = ''

while n > 0:
    result = str(n % 2) + result #2進数を表示するには文字列型
    n //= 2

print(result)