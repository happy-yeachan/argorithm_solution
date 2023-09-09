from sys import stdin
from collections import deque

n = int(stdin.readline())
if n == 1: # 미로의 크기가 1이면 건너지 않고 조건 만족
    print(0)
    exit()

maze = list(map(int,stdin.readline().split()))
visited = [0]*n
q = deque([(0,maze[0])]) # 위치와 점프 할 수 있는 거리

while q:
    p, j = q.popleft()
    for i in range(1,j+1):
        if p+i >= n or visited[p+i]:  # 미로의 최대 크기보다 넘어가는 곳으로 가거나 이미 방문한 곳이면 무시하고 계속 탐색
            continue
        visited[p+i] = visited[p]+1
        q.append((p+i,maze[p+i]))
if visited[n-1]:
    print(visited[n-1])
else: # 맨 마지막 미로를 밟을 수 없는 경우
    print(-1)