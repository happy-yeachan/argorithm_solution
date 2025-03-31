import sys
input = sys.stdin.readline
n = int(input())


office = []
for i in range(n):
    name, move = input().split()
    if move == "enter":
        office.append(name)
    else:
        office.remove(name)
office.sort(reverse=True)


for i in office:
    print(i)