def solution(num):
    if num == 1:
        return 0
    cnt = 0
    while num != 1 and cnt < 500:
        if num%2 == 0:
            num/=2
        else:
            num*=3
            num+=1
        cnt +=1
    if num != 1:
        return -1
    else:
        return cnt