# 2935_noise
A = int(input())
C = input()
B = int(input())
if (A % 10 == 0 or A==1) and (B% 10==0 or B==1):
    if C == "*":
        print(A*B)
    elif C == "+":
        print(A+B)
    else:
        print("error")
else:
    print("error")
A = int(input())
C = input()
B = int(input())
if (A % 10 == 0 or A==1) and (B% 10==0 or B==1):
    if C == "*":
        D=A*B
    elif C == "+":
        D=A+B
    else:
        print("error")
    if len(str(D))<=100:
        print(D)
    else:
        print("error")
else:
    print("error")