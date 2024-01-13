# 2675_string repetition
T = int(input())
if T>=1 and T<=1000:
    for _ in range(T):
        R, S = input().split()
        if int(R)>=1 and int(R)<=8 and len(S)>=1 and len(S)<=20:
            for i in S:
                print(i*int(R),end='')
            print()
        else:
            print("error")
else:
    print("error")