N, M = map(int, input().split())

li = [x for x in range(1, N+1)]

def swap(a, b):
    tmp = li[a-1]
    li[a-1] = li[b-1]
    li[b-1] = tmp

for _ in range(M):
    i, j = map(int, input().split())
    swap(i, j)

print(*li)