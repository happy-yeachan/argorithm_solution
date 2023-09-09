import sys
input = sys.stdin.readline

def back(cnt):
    if len(road) == m:
        for i in road:
            print(i, end=" ")
        print()
        return
    for i in range(cnt, n):
        if (i+1)not in road:
            road.append(i+1)
            back(i+1)
            road.pop()  



n, m = list(map(int, input().split()))
if m == 1:
    for i in range(n):
        print(i+1, end=" ")
    exit()

road = []
check = [False]*n
back(0)