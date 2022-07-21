a, b, *c = (0,1,3,4,5,6)

print(a)
print(b)
print(c)


scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)

# scores를  valid_score에 바인딩하기
