import sys

n = int(sys.stdin.readline())
tmp = []
for i in range(n):
    tmp.append(int(sys.stdin.readline()))

tmp.sort()
sum = 0
for i in range(n):
    sum += abs(i+1-tmp[i])

print(sum)