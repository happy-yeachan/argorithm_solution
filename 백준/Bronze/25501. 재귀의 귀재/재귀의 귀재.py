import sys
input = sys.stdin.readline
T = int(input())


def recursion(s, l, r, cnt):
    cnt += 1
    if(l >= r): 
        return "1 " + str(cnt)
    elif (s[l] != s[r]): 
        return "0 " + str(cnt)
    else: 
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)


for i in range(T):
    tc = input().strip()
    print(isPalindrome(tc))