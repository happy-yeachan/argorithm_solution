import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for i in range(N):
    site, password = input().split()
    dic[site.strip()] = password.strip()

for j in range(M):
    search = input()
    print(dic[search.strip()])