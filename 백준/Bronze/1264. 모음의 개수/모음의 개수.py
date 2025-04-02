import sys

input = sys.stdin.readline
mo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while 1:
    tmp = input().strip()
    if tmp == '#':
        break
    cnt = 0
    for i in range(len(tmp)):
        if tmp[i] in mo:
            cnt +=1
    print(cnt)

