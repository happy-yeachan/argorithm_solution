#1654 랜선자르기
#이진탐색 이용하면 될듯
k, n = map(int, input().split())
arr = []

for i in range(k):
    arr.append(int(input()))

#1부터 가장 긴 랜선의 길이를 가지고 이진탐색
s = 1
f = max(arr)

while (s <= f):
    mid = (s + f) // 2
    cnt = 0
    for i in range(k):
        cnt += arr[i] // mid  #나눠서 몇개의 랜선이 만들어지는지 확인
    if cnt >= n:
        s = mid + 1
    else:
        f = mid - 1

print(f)