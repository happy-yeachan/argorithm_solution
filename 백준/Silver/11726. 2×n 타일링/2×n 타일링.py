n = int(input())

if n <= 3:
    print(n)
else:
    li = [1, 2, 3]
    for i in range(3,n):
        li.append(li[i-2] + li[i-1])
    print(li[-1]%10007)