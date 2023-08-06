input_year = input('西暦: ')
def change_to_era(n):
    if  (1868 <= n) and (n <= 1911):
        if n == 1868:
            print('明治元年')
        else:
            print('明治' + str(n - 1867) + '年')
    elif (1912 <= n) and (n <= 1925):
        if n == 1912:
            print('大正元年')
        else:
            print('大正' + str(n - 1911) + '年')
    elif (1926 <= n) and (n <= 1988):
        if n == 1926:
            print('昭和元年')
        else:
            print('昭和' + str(n - 1925) + '年')
    elif (1989 <= n) and (n <= 2018):
        if n == 1989:
            print('平成元年')
        else:
            print('平成' + str(n - 1988) + '年')
    elif n == 2019:
        print('令和元年')
    else:
        print('令和' + str(n -2018) + '年')

if (1868 <= int(input_year)) and (int(input_year) <= 2020):
    print(change_to_era(int(input_year)))
else:
    print('1868から2020の数字を入力してください')