T=input() 
frequency = {} #빈도 딕셔너리를 만들어준다 
for i in T: 
    count = frequency.get(i,0) #get함수로 딕셔너리의 key로 value를 얻을 수 있다.
    frequency[i] = count + 1 
    
for j,k in frequency.items(): 
    print(f'{j},{k}')