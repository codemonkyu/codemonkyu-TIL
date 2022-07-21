a, b, *c = (0,1,3,4,5,6)

print(a)
print(b)
print(c)


scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)

# scores를  valid_score에 바인딩하기

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

print( "메로나 가격: " ,ice['메로나'])

#딕셔너리 인덱싱 
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

print(inventory["메로나"][0], "원")

inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

print(inventory["메로나"][1], "개")

