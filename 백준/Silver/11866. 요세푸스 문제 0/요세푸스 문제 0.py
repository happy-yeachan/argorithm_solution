N, K = map(int, input().split())

li = [ x+1 for x in range(N)]
result = '<'
pt = 0
while len(li):
    pt += K-1
    pt %= len(li)
    result+=str(li[pt])+ ', '
    li.remove(li[pt])

result = result[:-2] + '>'

print(result)