#3009_fourth point
ward = []
X, Y = 0, 0
for _ in range(3):
    A,B = map(int,input().split())
    if all(1<=x<=1000 for x in (A,B)):
           ward.append((A,B))
    else:
           print("error")
if ward[0][0]==ward[1][0]:
        X = ward[2][0]
elif ward[0][0]==ward[2][0]:
        X = ward[1][0]
else:
        X = ward[0][0]
if ward[0][1]==ward[1][1]:
       Y = ward[2][1]
elif ward[0][1]==ward[2][1]:
       Y = ward[1][1]
else:
       Y = ward[0][1] 
print(X, Y)