# 10103_dice game
n = int(input())
AO,BO=100,100
if 1<=n<=15:
    for _ in range(n):
        A,B = map(int,input().split())
        if all(1<=x<=6 for x in (A,B)):
            if A<B:
                AO-=B
            elif A>B:
                BO-=A
            else:
                continue
        else:
            print('error')
    print(AO)
    print(BO)
else:
    print('error')