# 5086_multiples and divisors
while True:
    A, B = map(int,input().split())
    if all(x<10000 for x in (A, B)):
        if A==B==0:
            break
        else:
            if A<B and B%A==0:
                print('factor')
            elif A>B and A%B==0:
                print('multiple')
            else:
                print('neither')
    else:
        print('error')