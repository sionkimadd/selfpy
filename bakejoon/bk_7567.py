# 7567_bowl
dish = list(input())
answer = 0
if 3<=len(dish)<=50:
    for i in range(len(dish)):
        if i == 0:
            answer += 10
        elif dish[i] == dish[i-1]:
            answer += 5
        else:
            answer += 10
    print(answer)
else:
    print("error")