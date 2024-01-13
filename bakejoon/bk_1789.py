# 1789_sum of numbers
S = int(input())
N = 1
if S>=1 and S<=4294967295:
    while (N*(N+1))//2 <=S:
        N+=1
    print(N-1)
else:
    print("error")
def max_n(S):
    n = 1
    while (n * (n + 1)) // 2 <= S:
        n += 1
    return n - 1
S = int(input())
print(max_n(S))