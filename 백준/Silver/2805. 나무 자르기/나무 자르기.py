# 쌩코딩 하니까 시간초과 안풀림
# 이분탐색 써야한다고 함

import sys

n, m = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(li)

# 이분 탐색을 위한 while문
# 오랜만
while left <= right:
    mid = (left + right) // 2
    tmp = 0

    # 중간 값에서 tmp를 이용해 문제에서 원하는 값이 맞는지 판단 
    for i in li:
        if i >= mid:
            tmp += i - mid

    # 원하는 값보다 작으면 오른쪽 파트에서 다시 한 번 이분탐색
    if tmp >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)