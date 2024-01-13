# 2525 오븐
H, M = map(int, input().split())
T = int(input())
if H>=0 and H<=23 and M>=0 and M<=59 and T>=0 and T<=1000:
    if H +((M+T)//60)>= 24 and M+T>=60:
        H1 = H +((M+T)//60)-24
        M1 = M+T-((M + T) // 60) * 60
        print("%d %d"%(H1,M1))
    elif H < 24 and M+T >= 60:
        H1 = H +((M+T)//60)
        M1 = M+T-((M + T) // 60) * 60
        print("%d %d"%(H1,M1))
    else:
        H1 = H
        M1 = M+T
        print("%d %d"%(H1,M1))
else:
    print("error")
H, M = map(int, input().split())
T = int(input())
if H>=0 and H<=23 and M>=0 and M<=59 and T>=0 and T<=1000:
        M1 = (M+T)//60 #
        M2 = (M+T)%60
        H1 = (H+M1)%24
        print("%d %d"%(H1,M2))
else:
    print("error")