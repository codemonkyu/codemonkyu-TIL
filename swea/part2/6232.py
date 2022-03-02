word="madam"

def function(T): 
    for i in range(len(T)//2): 
        if T[i]!=T[-1-i]: 
            return False
    return True 
print(word)

if function(word): 
    print("입력하신 단어는 회문(Palindrome)입니다.") 
else : 
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")
    
    


