import sys
input = sys.stdin.readline

# 알파벳의 갯수를 카운트
def count_word(li):
    li.sort()
    cnt_li = []
    tmp = li[0]
    cnt = 1
    hol = 0
    for i in range(1,len(li)):
        if li[i] == tmp:
            cnt += 1
        else:
            cnt_li.append((tmp,cnt))
            tmp = li[i]
            cnt = 1
    cnt_li.append((tmp,cnt))
    return cnt_li


li = list(input().rstrip())

cnt_li= count_word(li)

palindrome = []
hol = []
for i in cnt_li:
    if i[1]%2 == 0:
        for _ in range(i[1]//2):
            palindrome.append(i[0])
    elif not hol and i[1]%2 == 1:
        hol.append(i[0])
        for _ in range(i[1]//2):
            palindrome.append(i[0])
    else:
        print("I'm Sorry Hansoo")
        exit()
palindrome.sort()
left = palindrome
mid = hol
right = list(reversed(palindrome))
result = left + mid + right

print("".join(result))