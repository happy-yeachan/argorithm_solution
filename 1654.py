import sys

k, n = map(int, input().split())
arr = []

for i in range(k):
    arr.append(int(input()))

s = 1
f = max(arr)

while (s <= f):
    mid = (s + f) // 2
    cnt = 0
    for i in range(k):
        cnt += arr[i] // mid
    if cnt >= n:
        s = mid + 1
    else:
        f = mid - 1
print(f)