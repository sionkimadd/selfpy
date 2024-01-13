# 10039_average score
total = 0
for _ in range(5):
    i = int(input())
    if 0 <= i <= 100 and i%5==0:
        if i < 40:
            total += 40
        else:
            total += i
    else:
        print("error")
print(total//5)