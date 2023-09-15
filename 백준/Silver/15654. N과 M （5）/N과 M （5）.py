import sys
input = sys.stdin.readline

def back():
    if len(case) == m:
        for i in case:
            print(i, end=" ")
        print()
    for i in li:
        if i not in case:
            case.append(i)
            back()
            case.pop()



n, m = list(map(int, input().split()))

li = list(map(int, input().split()))
li.sort()
case = []

back()