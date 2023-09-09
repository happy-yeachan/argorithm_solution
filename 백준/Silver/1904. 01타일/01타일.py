n = int(input())

tmp = [1, 2]
for i in range(2, n):
    tmp.append((tmp[i-1]+tmp[i-2])%15746)

print(tmp[n-1])