N = int(input())
li = list(map(int, input().split()))

li.sort()

result = 0
for i in range(len(li)):
    result += li[i] * (len(li)-i)

print(result)
