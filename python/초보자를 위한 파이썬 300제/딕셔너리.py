from optparse import Values
from unittest import result


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

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys())
ice2 = list(icecream.values())
ice3 = sum(icecream.values())
print(ice)
print(ice2)
print(ice3)

# zip 과 dict 
keys = ("iphone","samsung","galaxy","apple")
Vals = (3000, 2000, 1000, 40000)
result = dict(zip(keys, Vals))
print(result)

