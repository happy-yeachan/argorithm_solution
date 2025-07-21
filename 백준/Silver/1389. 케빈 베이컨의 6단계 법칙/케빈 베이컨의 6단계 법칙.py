import sys

input = sys.stdin.readline

N, M = map(int, input().split())

li = [[] for _ in range(N+1)]

# 인접 리스트 생성
for i in range(M):
    A, B = map(int, input().split())
    li[A].append(B)
    li[B].append(A)

for i in range(N+1):
  li[i] = list(set(li[i]))

from collections import deque
# 사람마다 BFS 진행
def bfs(start):
    visit = [-1] * (N+1)
    visit[start] = 0
    q = deque()
    q.append(start)

    while q:
      now = q.popleft()
      for i in li[now]:
         if visit[i] == -1:
            visit[i] = visit[now] + 1
            q.append(i)
    
    return sum(visit[1:])

# 최소값을 가지는 번호 계산
min_value = 1e9
answer = 0

for i in range(1, N+1):
    tmp = bfs(i)
    if tmp < min_value:
        min_value = tmp
        answer = i

print(answer)