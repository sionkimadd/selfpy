# 10988_checking for a palindrome
p = input()
if 1<=len(p)<=100 and p.lower()==p:
    r = p[::-1]
    if p==r:
        print(1)
    else:
        print(0)
else:
    print('error')