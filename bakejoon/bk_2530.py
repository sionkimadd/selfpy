# 2530_artificial intelligence watch
H, M, S = map(int, input().split())
T = int(input())
if H>=0 and H<=23 and M>=0 and M<=59 and S>=0 and S<=59 and T>=0 and T<=500000:
        S1 = (S+T)%60
        M1 = (S+T)//60
        M2 = (M+M1)%60
        H1 = (M+M1)//60
        H2 = (H+H1)%24
        print("%d %d %d"%(H2,M2,S1))
else:
    print("error")