furniture = {"TV": 2000000,
"냉장고": 1500000,
"책상": 350000,
"노트북": 1200000,
"가스레인지": 200000,
"세탁기": 1000000}

i_dict = {i: furniture[i] for i in sorted(furniture, key=furniture.get, reverse=True)}
#sort랑 sorted 차이가 뭘까 ? 공부해보기
          

for key, value in i_dict.items():
    print(f'{key}: {value}')