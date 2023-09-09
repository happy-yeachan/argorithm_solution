import sys

def back():
    if len(check) == m:
        for i in check:
            print(i, end=" ")
        print()
    for i in range(1, n+1):
        if i not in check:
            check.append(i)
            back()
            check.pop()

input = sys.stdin.readline

n, m = list(map(int, input().split()))

check=[]

back()