# 2163_cutting chocolate
N, M = map(int,input().split())
if all(1<=x<=300 for x in(N, M)):
    print(N*M-1)
else:
    print("error")
T, A, B = map(int,input().split())
for i in range(1, T+1):
    print("Case #%d: %d" %(i, A+B))