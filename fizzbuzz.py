for i in range(1, 101): #1 <= i < 101 => 1 <= i <=100
    if i % 15 == 0:
        print('FizzBuzz', end=' ') #end=' 'を要素に付け加えると改行せずに空白を出力する
    elif i % 3 == 0:
        print('Fizz', end=' ')
    elif i % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(i, end=' ')