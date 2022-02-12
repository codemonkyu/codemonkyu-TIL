import datetime

name = input()
age=int(input())
p_age=datetime.datetime.now().year-3+(100-age)

print(f'{name}(은)는 {p_age}년에 100세가 될 것입니다.')