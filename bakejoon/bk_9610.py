# 9610_quadrant
n = int(input())
Q1,Q2,Q3,Q4,Axis=0,0,0,0,0
if 1<=n<=1000:
    for _ in range(n):
        x, y = map(int,input().split())
        if all(-10**6<=a<=10**6 for a in (x,y)):
            if x>0 and y>0:
                Q1 += 1
            elif x<0 and y>0:
                Q2 += 1
            elif x<0 and y<0:
                Q3 += 1
            elif x>0 and y<0:
                Q4 += 1
            else:
                Axis +=1
        else:
            print('error')
    print('Q1: %d' % Q1)
    print('Q2: %d' %Q2)
    print('Q3: %d' %Q3)
    print('Q4: %d' %Q4)
    print('AXIS: %d' %Axis)
else:
    print('error')