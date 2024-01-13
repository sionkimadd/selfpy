# 10757_large number A+B
A,B = map(int,input().split())
if all(0<x<10**10000 for x in (A,B)):
    print(A+B)
else:
    print('error')
