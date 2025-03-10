test_case = int(input())
for i in range(test_case):
    n = int(input())
    clothes = {}
    for j in range(n):
        a, b = input().split()
        if b not in clothes:
            clothes[b]=1
        else:
            clothes[b] += 1
    sum = 1
    for k in clothes:
        sum *= clothes[k] + 1
    print(sum-1)
