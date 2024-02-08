def solution(s):
    answer = True
    tmp = 0
    for i in range(len(s)):
        if s[i] == "p" or s[i] == "P":
            tmp += 1
        elif s[i] == "y" or s[i] == "Y":
            tmp -= 1
    if tmp == 0:
        return True
    else:
        return False
