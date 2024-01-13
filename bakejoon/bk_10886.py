# 10886_0 = not cute / 1 = cute
N = int(input())
B = []
if N in range(1,102,2):
    for _ in range(N):
        A = int(input())
        if A in [0,1]: 
            B.append(A)
        else:
            print("error")
    zero =B.count(0)
    one = B.count(1)
else:
    print('error')
if zero>one:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')