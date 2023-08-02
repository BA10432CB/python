#money = 10000
#price = 2362
#def vending_machine():
#    change = money - price
#    print(change)
#
#vending_machine()

#money = input('insert:')
#price = input('price:')
#def vending_machine():
#    change = int(money) - int(price)
#    print('change:' + str(change))
#お釣りの枚数の計算    
#    change_5000 = (change // 5000)
#    change_1000 = ((change - (change_5000 *5000)) // 1000)
#    change_500  = ((change - (change_5000*5000)-(change_1000*1000)) // 500)
#    change_100  = ((change - (change_5000*5000)-(change_1000*1000)-(change_500*500)) // 100)
#    change_50   = ((change - (change_5000*5000)-(change_1000*1000)-(change_500*500)-(change_100*100)) // 50)
#    change_10   = ((change - (change_5000*5000)-(change_1000*1000)-(change_500*500)-(change_100*100)-(change_50*50)) // 10)
#    change_5    = ((change - (change_5000*5000)-(change_1000*1000)-(change_500*500)-(change_100*100)-(change_50*50)-(change_10*10)) // 5)
#    change_1    = change - (change_5000*5000)-(change_1000*1000)-(change_500*500)-(change_100*100)-(change_50*50)-(change_10*10)-(change_5*5)
#    print('5000:' + str(change_5000))
#    print('1000:' + str(change_1000))
#    print('500:' + str(change_500))
#    print('100:' + str(change_100))
#    print('50:' + str(change_50))
#    print('10:' + str(change_10))
#    print('5:' + str(change_5))
#    print('1:' + str(change_1))

#vending_machine()

money = input('insert:')
price = input('price:')
change = int(money) - int(price)

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]

for i in coin:
    r = change // i
    change %= i
    print(str(i) + ':' + str(r))