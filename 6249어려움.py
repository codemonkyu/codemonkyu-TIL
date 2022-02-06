
number = str(input())

result=[0]*10

for i in number:
    result[int(i)] += 1 # i는 str로 int화해준다
    #print(result)

# temp=[0,1,2,3,4,5,6,7,8,9]

for j in range(10):
    if j == 9:
        print(j)
    else:
        print(j,end=' ')
    

for k in range(10):
    if k == 9:
        print(0)
    else:
        print(result[int(k)],end=' ')

    
  