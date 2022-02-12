def function(*arg):
    a = 1
    for i in arg:
        if type(i) != int(i):
            print('에러발생')
        else:
            a *= i
    
    return a

#*arg 는 가변인자를 위한 함수 (함수인자를 몇개 받을지 모르는경우)
#따라서 result라는 변수를 주고 가변인자를 *= += 등으로 받아준다.
