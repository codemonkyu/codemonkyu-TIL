a = input()

def function(a):
    b = a[::-1] #문자열을 반대로 -> 문자열[::-1]
    
    if a == b:
        return("입력하신 단어는 회문(Palindrome)입니다.")
        
print(a)
print(function(a))