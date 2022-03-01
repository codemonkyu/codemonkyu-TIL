T = input().strip()
a = 0
b = 0

for i in T:
    if 'a' <= i <= 'z' :
        a += 1
    elif 'A' <= i <= 'Z':
        b += 1
        
print(f'UPPER CASE {a}')
print(f'LOWER CASE {b}')
