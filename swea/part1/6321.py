# def function(a):
#     if a == 1:
#         print("소수가 아닙니다.")
#         return
    
#     for i in range(2,a):
#         if a%i == 0:
#             print("소수가 아닙니다.")
#             return
            
#     else:
#         print("소수입니다.")
        

# a=int(input())
# function(a)
          
    
a = int(input())

def funciton(a):
    cnt = 1
    while True:
        cnt += 1
        if cnt == a:
            print("소수입니다.")
            break
        if cnt % a == 0:
            print("소수가아닙니다.")
            break   

funciton(a)
    
  