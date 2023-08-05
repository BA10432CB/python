import sys

input_price = input('insert: ')
if not input_price.isdecimal():
    print('整数を入力してください')
    sys.exit()

product_price = input('product: ')
if not product_price.isdecimal():
    print('整数を入力してください')
    sys.exit()

change = int(input_price) - int(product_price)

if change < 0:
    print('金額が不足しています')
    sys.exit()

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r, change = divmod(change, i)
    # r = change // i #お釣りを各要素で割った商をrに代入する
    # change %= i #お釣りを各要素で割った余りをchangeに代入して更新
    print(str(i) + ': ' + str(r)) #出力