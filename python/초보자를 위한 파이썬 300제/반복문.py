## for 문 
for i in ["A", "B", "C"]:
    b = i.lower()

print("변환: ", b)



list = [10, 20, 30]
for i in list:
    print(i)
    

#141
list = [100, 200, 300]

for i in list:
    b = i + 10
    print(b)
    
#142
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print("오늘의 메뉴 :", i)
    
    
#148
리스트 = ["가", "나", "다", "라"]
for i in 리스트[1:]:
    print(i)
    
#149
리스트 = ["가", "나", "다", "라"]


#151
리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i < 0:
        print(i)
    
#152    
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i % 3 == 0:
        print(i)
        
#153
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if (i % 3 == 0) and (i < 20):
        print(i)
        
#154
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if str(i) >= str(3):
        print(i)
    elif len(i) >= 3:
        print(i)  
        
#155
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.isupper():
        print(i)
        
#156
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if not i.isupper():
        print(i)
        
#157
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i[0].upper() + i[1:])

#158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트:
    j = i.split(".")
    print(j[0])
    
#159
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    j = i.split(".")
    if j[1] == "h":
        print(i)
        
#160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    j = i.split(".")
    if j[1] == "h" or j[1] == "c":
        print(i)
        
#161 for & range
for i in range(2002, 2051, 4):
    print(i)
    
#163
for i in range(3, 31, 3):
    print(i)
    
#166 f스트링사용
for i in range(1, 10):
    print(f'3x{i} =', i * 3)
    
    
#168 
j = 0
for i in range(1, 11):
    j += i
print(f'합 : {j}')

#169 홀수만
j = 0
for i in range(1, 11, 2):
    j += i
print(f'합 : {j}')

#170 곱하기
j = 1
for i in range(1, 11):
    j *= i
    print(f'{j}')

#171 len함수
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])
    
#172 enumerate사용
price_list = [32100, 32150, 32000, 32500]
for i, data in enumerate(price_list):
    print(price_list[i])


#173
price_list = [32340, 32310, 32310, 32320]
for i, data in enumerate(price_list):
    print(price_list[i])
