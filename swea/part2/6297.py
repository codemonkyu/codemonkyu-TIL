a = map(int,input().split(','))
b = [ i for i in a if i%2 ==1 ]

print(str(b))
b_str = str(b)[1:-1]

print(b_str)
