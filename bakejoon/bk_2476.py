#2476_dice game
N = int(input())
em = []
if 2<=N<=1000:
    for _ in range(N):
        A, B, C = map(int,input().split())
        if all(1<=x<=6 for x in (A,B,C)):
            if A==B==C:
                same =10000+A*1000
            elif A==B or B==C or A==C:
                if A==B:
                    same =1000+A*100
                elif B==C:
                    same =1000+B*100
                else:
                    same =1000+A*100
            else:
                max_num = max(A,B,C)
                same =max_num*100
        else:
            print("error")
        em.append(same)
    high_same=max(em)
    print(high_same)
else:
    print("error")