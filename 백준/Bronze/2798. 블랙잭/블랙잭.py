from itertools import combinations
N, M = map(int, input().split())

li = list(map(int, input().split()))
pick = list(combinations(li, 3))
result = 0
for i in pick:
    if sum(i) <= M:
        result = max(result, sum(i))

print(result)