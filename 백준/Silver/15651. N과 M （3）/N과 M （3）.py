import sys

input = sys.stdin.readline

def back():
    if len(check) == m:
        print(*check)
        return
    for i in range(1, n+1):
        check.append(i)
        back()
        check.pop()

n, m = list(map(int, input().split()))

check=[]

back()