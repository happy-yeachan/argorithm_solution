import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visit = [-1] * n

    while q:
        x, y = q.popleft()

        if abs(rx- x) + abs(ry - y) <= 1000:
            return "happy"
        for i in range(n):
            if visit[i] == -1:
                nx, ny = p_li[i]
                if abs(nx -x) + abs(ny-y) <= 1000:
                    visit[i] = 1
                    q.append((nx, ny))
    return "sad"

for i in range(t):
    # 편의점의 개수 n
    n = int(input())
    
    # 상근이네 집 좌표
    sx, sy = map(int, input().split())
    
    # 편의점 좌표
    p_li = [list(map(int, input().split())) for _ in range(n)]
    
    # 락 페스티벌 좌표
    rx, ry = map(int, input().split())

    print(bfs(sx, sy))
    
