i = int(input())
a = ''

while i>0:
    a += str(i%2) 
    i//=2 #이진법이니까
    
print(a)
