

N, M = map(int, input().split())

li = {}

for i in range(N):
    ip = input()
    li[ip] = i+1
    li[i+1] = ip

result = []
for j in range(M):
    tmp = input()
    try:
        tmp = int(tmp)
        result.append(li[tmp])
    except:
        result.append(li[tmp])

for _ in result:
    print(_)
