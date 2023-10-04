def solution(n):
    cnt1 = bin(n).count("1")
    tmp = 1
    while True:
        n += 1
        cnt1_2 = bin(n).count("1")
        if cnt1 == cnt1_2:
            break
    return n