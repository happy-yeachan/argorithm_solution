import sys

input = sys.stdin.readline

# f - 총 층수
# s - 현재 층
# g - 스타트링크의 층
# u - 위로 u칸 가는 버튼
# d - 아래로 d칸 가는 버튼

f, s, g, u, d = list(map(int, input().split()))
if s==g:
    print(0)
    exit()
depth = [0] * (f+1)
check = [False] * (f+1)
check[s] = True
from collections import deque

q = deque()
q.append(s)

while(q):
    now = q.popleft()
    if depth[g] != 0:
        print(depth[g])
        exit()

    for i in [u, -d]:
        next = now + i
        if 0< next and next<=f:
            if not check[next]:
                q.append(next)
                depth[next] = depth[now] + 1 
                check[next] = True

print("use the stairs")