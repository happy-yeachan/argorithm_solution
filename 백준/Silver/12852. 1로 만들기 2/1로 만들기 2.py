from collections import deque

n = int(input())
q = deque()
q.append([n])


def bfs():
    while q:
        arr = q.popleft()

        x = arr[0]
        if x == 1:
            return arr

        if x % 3 == 0:
            q.append([x//3] + arr)

        if x % 2 == 0:
            q.append([x//2]+arr)

        q.append([x-1]+arr)

res = bfs()
print(len(res)-1)
print(*res[::-1])