from sys import stdin

input = stdin.readline

N = int(input())
li = []
for i in range(N):
    a = list(input().split())
    if a[0] == "push":
        li.append(a[1])
    elif a[0] == "pop":
        if len(li)!=0:
            print(li.pop(0))
        else:
            print(-1)
    elif a[0] == "size":
        print(len(li))
    elif a[0] == "empty":
        if len(li) != 0:
            print(0)
        else:
            print(1)
    elif a[0] == "front":
        if len(li)!=0:
            print(li[0])
        else:
            print(-1)
    elif a[0] == "back":
        if len(li)!=0:
            print(li[-1])
        else:
            print(-1)
