# 1977_perfect square number
# M = int(input()) ; N = int(input())
# if all(1<= x <=10000 for x in (M,N)) and N>M:
#     i = 0
#     box = []
#     for num in range(M,N+1):
#         for num in range(M):
#             i+=1
#             if i == M/i:
#                 box.append(M)
#             else:
#                 pass
#         i = 0
#         M+=1
#     result = sum(box)
#     if box:
#         print(result)
#         print(box[0])
#     else:
#         print(-1)   
# else:
#     print("error")
import sys   
import math
M = int(sys.stdin.readline()) 
N = int(sys.stdin.readline())
box=[]
if all(1<= x <=10000 for x in (M,N)) and N>M:
    if math.isqrt(M)**2 == M: #start = math.isqrt(M) if math.isqrt(M)**2 == M else math.isqrt(M) + 1
        start = math.isqrt(M)
    else: 
        start = math.isqrt(M) + 1 
    end = math.isqrt(N) 
    for i in range(start, end+1): #box = [i**2 for i in range(start, end+1)]  
        box.append(i**2)
    if box: 
        print(sum(box)) 
        print(box[0]) 
    else: 
        print(-1) 
else:
    print("error")
if math.isqrt(M)**2 == M:
    start = math.isqrt(M)
else:
    math.isqrt(M) + 1