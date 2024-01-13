# 5063_TGN
TGN = int(input())
for _ in range(TGN):
    r,e,c = map(int,input().split())
    if all(-10**6<=x<=10**6 for x in (r,e)) and 0<=c<=10**6:
        if r+c<e:
            print('advertise')
        elif r+c>e:
            print('do not advertise')
        else:
            print('does not matter')
    else:
        print('error')