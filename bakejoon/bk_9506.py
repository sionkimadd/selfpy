# 9506_sum of divisors
while True:
    n = int(input())
    q = []
    if n == -1:
        break
    if 2<n<100000:
        for i in range(1, n):
            if n % i == 0:
                q.append(i)
        if sum(q) == n:
            print(n, " = ", " + ".join(str(i) for i in q))
        else:
            print(n, "is NOT perfect.")
    else:
        print('error')