x = 3
def calc(x):
    x += 4
    return x

print(x) #3
print(calc(x)) #7
print(x) #3

a = [3]
def calc(a):
    a[0] += 4
    return a

print(a) #[3]
print(calc(a)) #[7]
print(a) #[7]

b = [3]
def calc(b):
    b = [4]
    return b

print(b) #[3]
print(calc(b)) #[4]
print(b) #[3]