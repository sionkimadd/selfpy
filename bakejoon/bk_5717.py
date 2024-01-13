# 5717_sanggeun's friends
while True:
    M, F = map(int,input().split())
    if M==F==0:
        break
    else:
        if all(1<=x<=5 for x in (M,F)):
            print(M+F)
        else:
            print('error')