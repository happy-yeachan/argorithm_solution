import sys
input = sys.stdin.readline

def back(cnt):
    if len(road) == m:
        for i in road:
            print(i, end=" ")
        print()
        return
    for i in range(cnt, n):
        road.append(i+1)
        back(i)
        road.pop()

n, m = list(map(int, input().split()))

road = []

back(0)