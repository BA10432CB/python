# コンストラクタの定義　def 戻り値以外には文末に：をつける
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)

# print()で出力
for i in range(8):
    print(fibonacci(i))