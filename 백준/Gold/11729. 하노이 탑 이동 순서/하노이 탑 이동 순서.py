import sys
def hanoi(cnt, start, target, support):
    if cnt == 1:
        result.append([start, target])
        return
    hanoi(cnt-1,start, support, target)
    result.append([start, target])
    hanoi(cnt-1, support, target, start)

input = sys.stdin.readline

n = int(input())
result = []
hanoi(n, 1, 3, 2)

print(len(result))
for i in result:
    print(" ".join(list(map(str, i))))