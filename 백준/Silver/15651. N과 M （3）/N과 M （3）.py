import sys
input = sys.stdin.readline

def back():
    if len(road) == m:
        for i in road:
            print(i, end=" ")
        print()
        return
    for i in range(n):
        road.append(i+1)
        back()
        road.pop()

n, m = list(map(int, input().split()))

road = []

back()