words = [w for w in input().split(', ')]

words.sort()
for i in words[:-1]:
    print("{}, ".format(i), end='')
    
print(words[-1])