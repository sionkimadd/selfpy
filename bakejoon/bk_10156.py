# 10156_snack
K, N, M = map(int,input().split())
if all(1<=x<=1000 for x in (K,N)) and 1<=M<=100000:
    if M<K*N:
        print(K*N-M)
    else:
        print(0)
else:
    print("error")