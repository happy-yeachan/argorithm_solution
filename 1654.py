#랜선 자르기
import math

k, n = map(int, input().split())
li = []
for i in range(0,k):
    li.append(int(input()))

max1 = math.gcd(*li)
tmp = sum(li)/n
tmp2 = sum(li)/(n+1)


print(max1, tmp, tmp2)