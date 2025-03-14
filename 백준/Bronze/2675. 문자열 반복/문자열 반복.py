T = int(input())
result = []
for i in range(T):
    A, B = input().split()
    tmp = ""
    for j in range(len(B)):
        tmp += (B[j] * int(A))
    result.append(tmp)

for i in result:
    print(i)