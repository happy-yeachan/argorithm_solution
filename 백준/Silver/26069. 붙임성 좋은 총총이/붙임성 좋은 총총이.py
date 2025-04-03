import sys

input = sys.stdin.readline

N = int(input())

rainbow = ['ChongChong']

for i in range(N):
    a, b = input().strip().split()
    if a in rainbow and b not in rainbow:
        rainbow.append(b)
    elif a not in rainbow and b in rainbow:
        rainbow.append(a)


print(len(rainbow))