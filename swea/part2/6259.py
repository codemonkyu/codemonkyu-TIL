T = input().strip()
a = 0
b = 0

for i in T:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        a += 1
    elif '0' <= i <= '9':
        b += 1
        
print(f'LETTERS {a}')
print(f'DIGITS {b}')
