a=[1,1]

def function(T):
    for i in range(0, T-2):
        a.append(a[i]+a[i+1])
    print(a)

T=int(input())
function(T)