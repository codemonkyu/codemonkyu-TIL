# a = input()
# b = input()
# c = input()
# d = input()
# e = input()

# sum = a+b+c+d+e

# print(f'입력된 값 [{a,b,c,d,e}]의 평균은 {sum/5}입니다.')

a=[int(input()) for i in range(5)]

print(f'입력된 값 {a}의 평균은 {sum(a)/5}입니다.')
