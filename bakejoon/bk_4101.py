# 4101_is it big?
A = 1
B = 1
while A!= 0 and B!=0:
    AA, BB = map(int,input().split())
    A=AA
    B=BB
    if A>B:
        print("Yes")
    elif A==B==0:
        break
    else:
        print("No")