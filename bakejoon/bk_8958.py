# 8958_OX Quiz
N = int(input())
for _ in range(N):
    A = list(input())
    if 0<len(A)<80:
        em = 0
        temp = 0
        for char in A:
            if char == 'O':
                temp +=1
                em +=temp
            elif char =='X':
                temp = 0
            else:
                print('error')
                break
        else:
            print(em)
    else:
        print('error')