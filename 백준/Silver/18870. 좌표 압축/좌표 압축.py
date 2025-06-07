N = int(input())
li = list(map(int, input().split()))

result = [0 for i in range(N)]
tmp = sorted(set(li))

rank = {num: i for i, num in enumerate(tmp)}

print(*(rank[num] for num in li))