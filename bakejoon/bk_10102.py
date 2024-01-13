# 10102_vote counting
V = int(input())
p = list(input())
if 1<=V<=15:
    if all(i in['A','B'] for i in p):
        if len(p) == V:
            A = p.count('A')
            B = p.count('B')
            if A>B:
                print('A')
            elif B>A:
                print('B')
            else:
                print('Tie')
        else:
            print('error')
    else:
        print('error')
else:
    print('error')