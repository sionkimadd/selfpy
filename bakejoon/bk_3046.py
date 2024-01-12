# 3046_R2
R1, R3 = map(int,input().split())
if all(-1000<=x<=1000 for x in(R1, R3)):
    print(2*R3-R1)
else:
    print("error")