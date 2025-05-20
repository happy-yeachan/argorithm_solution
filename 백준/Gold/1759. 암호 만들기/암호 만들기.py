import sys
input = sys.stdin.readline

def check(password):
    mo = sum (1 for x in password if x in 'aeiou')
    ja = len(password) - mo
    return mo >= 1 and ja >= 2

def back(idx, password):
    if len(password) == L:
        if check(password):
            print(password)
        return
    for i in range(idx, len(li)):
        password += li[i]
        back(i+1, password)
        password = password[:-1]


L, C = map(int, input().split())
li = list(input().split())

li = sorted(li)
back(0, "")

