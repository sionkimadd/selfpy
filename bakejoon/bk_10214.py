# 10214_baseball
T = int(input())
for i in range(T):
    a,b = 0,0
    for j in range(9):  
        y,k=map(int,input().split())
        a+=y
        b+=k
    if a>b:
        print('Yonsei')
    elif a<b:
        print('Korea')
    else:
        print('Draw')