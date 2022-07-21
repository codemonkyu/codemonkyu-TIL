list = [(90,80),(85,75),(90,100)]

a=list[0][0]+list[0][1]
b=list[1][0]+list[1][1]
c=list[2][0]+list[2][1]


for i in range(1,4):
    if i == 1:
        print(f'{i}번 학생의 총점은 {a}점이고, 평균은 {a/2}입니다.')
    elif i == 2:
        print(f'{i}번 학생의 총점은 {b}점이고, 평균은 {b/2}입니다.')
    elif i == 3:
        print(f'{i}번 학생의 총점은 {c}점이고, 평균은 {c/2}입니다.')

        
    
    
for i in list:
    print(f'{list.index(i)+1}번 학생의 총점은 {sum(i)}점이고, 평균은 {sum(i)/2}입니다.') 