# 11021_A+B - 7
T = int(input())
for i in range(1, T+1):
    A, B = map(int,input().split())
    if A>0 and B<10:
        print("Case #%d: %d" %(i, A+B))
    else:
        print("error")
T = int(input())
results = []
for i in range(1, T+1):
    A, B = map(int, input().split())
    if A > 0 and B < 10:
        results.append("Case #%d: %d" % (i, A + B))
    else:
        results.append("error")
for result in results:
    print(result)