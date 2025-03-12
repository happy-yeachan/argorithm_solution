N = int(input())
li = []

for i in range(N):
    age, name = input().split()
    li.append([age, name])

li.sort(key=lambda x:int(x[0]))
for i in range(N):
    print(li[i][0], li[i][1])