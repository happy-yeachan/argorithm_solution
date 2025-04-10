K = int(input())

li = []

for i in range(K):
    tmp = int(input())
    if tmp == 0:
        li.pop()
    else:
        li.append(tmp)

print(sum(li))