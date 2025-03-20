import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    li = list(input().split())
    while 1:
        say = list(input().split())
        if say[0] == "what":
            for j in li:
                print(j, end=" ")
            break
        while say[-1] in li:
            li.remove(say[-1])