x = 10

def reset():
    global x
    x = 30
    print(x)

reset() #関数内のグローバル変数xが採用
print(x) #関数内のグローバル変数xが採用