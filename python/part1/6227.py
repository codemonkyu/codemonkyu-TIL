for i in range(100,301):
    i=str(i)
    if int(i[0])%2 ==0 and int(i[1])%2 ==0 and int(i[2])%2 == 0:
        if int(i) == 288:
            print(i)
        else:
            print(i, end=',')


