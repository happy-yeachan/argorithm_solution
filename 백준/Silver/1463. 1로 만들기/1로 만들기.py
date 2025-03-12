n = int(input())

li = [0, 0, 1, 1]

if n <= 3:
    print(li[n])
else:
    for i in range(4,n+1):
        tmp = i
        if i % 3 == 0:
            tmp = li[i//3]
        if i % 2 == 0:
            tmp = min(tmp, li[i//2])
        tmp = min(tmp, li[i-1])
        li.append(tmp+1)
    print(li[-1])