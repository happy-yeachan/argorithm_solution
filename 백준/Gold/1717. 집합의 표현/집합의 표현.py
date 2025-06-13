import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
li = [i for i in range(n + 1)]

def find(x):
    if li[x] != x:
        li[x] = find(li[x])  # 경로 압축
    return li[x]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        li[b_root] = a_root

for _ in range(m):
    f, a, b = map(int, input().split())
    if f == 0:
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")
