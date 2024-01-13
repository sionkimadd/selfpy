# 11557_yangjojang of The Year
T = int(input())
for _ in range(T):
    N = int(input())
    if not (1 <= N <= 100):  
        print('error')
        continue
    max = 0
    mName = ""
    for _ in range(N):
        name, num = input().split()
        num = int(num)
        if not (1 <= len(name) <= 20) or not (0 <= num <= 10_000_000): 
            print('error')
            break
        if num > max:
            max = num
            mName = name
    else:  
        print(mName)