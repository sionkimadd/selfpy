# 11653_factorization
N = int(input())
d=2
if N>=1 and N<=10000000:
    while N != 1:
        if N % d != 0:
            d += 1
        else:
            N//=d
            print(d)
else:
    print("error")