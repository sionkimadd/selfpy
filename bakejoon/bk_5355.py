# 5355_mars math
case = int(input())
for _ in range(case):
    mars = list(map(str, input().split()))
    answer = 0
    if float(mars[0])>=0 and float(mars[0])<=100:
        for i in range(len(mars)):
            if i == 0:
                answer += float(mars[i])
            else:
                if mars[i] == "@":
                    answer *= 3
                elif mars[i] == "%":
                    answer += 5
                elif mars[i] == "#":
                    answer -= 7
        print("%0.2f" % answer)
    else:
        print("error")