#うるう年を出力するプログラム
def leap_year(n):
    if n % 4 == 0:
        if (n % 100 == 0) and (n % 400 != 0):
            return False
        else:
            return True
    else:
        return False

for i in range(1950, 2051):
    if leap_year(i):
        print(i, end=' ')