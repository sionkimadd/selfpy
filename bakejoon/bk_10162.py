# 10162_microwave
T = int(input())
a=[0,0,0]
if 1<=T<=10000:
    while T>=300:
            T-=300
            a[0]+=1
    while T >= 60:
            T -=60
            a[1]+=1
    while T>=10:
            T -= 10
            a[2]+=1
else:
       print('error')
if T>0:
       print(-1)
else:
      print(*a)