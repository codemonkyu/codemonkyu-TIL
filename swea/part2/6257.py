fruit = ['apple','banana','melon']
# strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
# lstrip([chars]) : 인자로 전달된 문자를 String의 왼쪽에서 제거합니다.
# rstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다.

# new_fruit={}

new_fruit = {fruit[i].strip():len(fruit[i].strip()) for i in range(0,len(fruit))}
print(new_fruit)


