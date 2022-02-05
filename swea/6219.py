num=int(input())

a=0
for i in range(1,num+1):
    if num %i == 0:
        a += 1
        print("%d(은)는 %d의 약수입니다."%(i,num))
    if a == 2:
        print("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다."%(num,1,num))
        
#a를 변수로 두어서 약수가 2개일때는 소수임을 알려준다.