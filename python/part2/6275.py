a = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
b =list('aeiou')
    

c = [i for i in a if i not in b]

print(''.join(c))
