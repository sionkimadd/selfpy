# 2588_multiplication
A = int(input())
B = int(input())
if all(100<= x <=999 for x in (A,B)):
    third_B = int(str(B)[2])
    second_B = int(str(B)[1])
    first_B = int(str(B)[0])
    print(A*third_B)
    print(A*second_B)
    print(A*first_B)
    print(A*B)
else:
    print("error")