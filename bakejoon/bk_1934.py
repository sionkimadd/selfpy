#1934_least common multiple
T = int(input())
if 1<=T<=1000:
    for _ in range(T):
        A, B = map(int,input().split())
        AA,BB=A,B
        if all(1<=x<=45000 for x in(A,B)):
            while A%B!=0:
                A,B=B,A%B
            print(AA*BB//B)
        else:
            print("error")