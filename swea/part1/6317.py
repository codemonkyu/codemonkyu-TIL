
# a = (3, 5, 4, 1, 8, 10, 2)
# b = max(a)


# print(f'max{a} => {b}')

b = (3, 5, 4, 1, 8, 10, 2)
def function(*args):
    a = 0
    for i in b:
        if i == max(b):
            a += i
        else:
            return
        
    print(f'max{b} => {a}')