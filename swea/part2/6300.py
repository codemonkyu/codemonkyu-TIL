a = [12, 24, 35, 70, 88, 120, 155]

b = [ i for i in a if a.index(i)%2 == 1]

print(b)