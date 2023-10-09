import sys


def back(inx):
    if len(tmp) == m:
        print(" ".join(list(map(str, tmp))))
        return
    for i in range(inx, n):
        tmp.append(li[i])
        back(i)
        tmp.pop()


input = sys.stdin.readline

n, m = map(int, input().split())

li = list(map(int, input().split()))
li.sort()

if m == 1:
    for i in li:
        print(i)
    exit()
tmp = []
result = []
back(0)
