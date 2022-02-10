lst=['가위','바위','보']
a_1=input()
b_1=input()

def function(a,b):
    if a==lst[0] and b==lst[1]:
        print("바위가 이겼습니다!")
    elif a==lst[1] and b==lst[2]:
        print("보가 이겼습니다!")
    elif a==lst[2] and b==lst[0]:
        print("가위가 이겼습니다!")
    elif a==lst[1] and b==lst[0]:
        print("바위가 이겼습니다!")
    elif a==lst[0] and b==lst[2]:
        print("가위가 이겼습니다!") 

a=input()
b=input()
function(a,b)