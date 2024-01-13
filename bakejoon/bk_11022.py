# 11022_A+B - 8
T = int(input())
results = []
for i in range(1, T+1):
    A, B = map(int, input().split())
    if A > 0 and B < 10:
        results.append("Case #%d: %d + %d = %d" % (i, A, B, A + B))
    else:
        results.append("error")
for result in results:
    print(result)