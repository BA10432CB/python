memo = {1: 1, 2: 1} #終了条件を辞書に保存
def fibonacci(n):
    if n in memo:
        return memo[n] #辞書に登録されていれば、その値を返す
    memo[n] = fibonacci(n - 2) + fibonacci(n - 1) #登録がなければ辞書に登録する
    return memo[n]