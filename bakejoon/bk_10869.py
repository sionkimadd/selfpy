# 10869_사칙연산
A, B = map(int, input().split())
if A>=1 and B<=10000:
    print(A+B)
    print(A-B)
    print(A*B)
    print(A//B)
    print(A%B)
else:
    print("error")