# 10817_wash face
A, B, C = map(int,input().split())
if all(1 <= x <= 100 for x in (A, B, C)):
    if B<=A<=C or C<=A<=B:
        print(A)
    elif A<=B<=C or C<=B<=A:
        print(B)
    elif A<=C<=B or B<=C<=A:
        print(C)
    else:
        print(A)
else:
    print("error")