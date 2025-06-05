# 모든 경우를 다 비교해봐도 될듯
# N의 최대 크기가 8이라 다 비교해도 8! * 8 는 얼추 32만번 임 충분
from itertools import permutations

N = int(input())
lis = list(map(int, input().split()))

result = 0
for li in permutations(lis):
    total = 0
    for i in range(N - 1):
        total += abs(li[i] - li[i + 1])
    result = max(result, total)

print(result)