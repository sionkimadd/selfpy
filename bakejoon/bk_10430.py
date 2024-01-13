#10430_remain
A, B, C = map(int, input().split())
if all(2 <= x <= 10000 for x in (A, B, C)):
    print((A+B)%C)
    print(((A%C)+(B%C))%C)
    print(A*B%C)
    print(((A%C)*(B%C))%C)
else:
    print("error")