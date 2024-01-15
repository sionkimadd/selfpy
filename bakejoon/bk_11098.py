# 11098_Help Chelsea!
import sys
n = int(sys.stdin.readline())
if n<=100:
    for _ in range(n):
        p = int(input())
        if 1<=p<=100:
            nName = '' 
            max = 0
            nums= []
            for _ in range(p):
                num, name = input().split(maxsplit=1)
                num = int(num)
                if " " in name or not(1<= len(name)<=20) or not(num<2*10**9) or num in nums:
                    print('error')
                    break
                if num > max:
                    max = num
                    nName = name
                nums.append(num)
            else:
                print(nName)
        else:
            print('error')
else:
    print('error')