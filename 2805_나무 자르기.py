import sys

n, m = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(li)

while left <= right:
    mid = (left + right) // 2
    total = 0

    for i in li:
        if i >= mid:
            total += i - mid

    if total >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)