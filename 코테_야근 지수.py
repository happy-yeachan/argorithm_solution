def solution(n, works):
    # 야근을 하기전에 일이 끝남
    if sum(works) < n:
        return 0
    works.sort(reverse=True)
    tmp = n
    idx = 0
    for i in range(len(works)-1):
        a = (works[i] - works[i+1])*(i+1)
        print(tmp, a)
        if tmp >= a:
            idx = i+1
            tmp -= a
        else:
            idx = i
            break
    m = tmp // (idx+1)
    p2 = tmp % (idx+1)
    print(works)
    print(idx, m,p2)
    if tmp != n:
        for i in range(idx+1):
            works[i] = works[idx] - m
    for i in range(p2):
        works[works.index(max(works))] -= 1
    print(works)
    for i in range(len(works)):
        if works[0] == 0:
            continue
        works[i] = works[i] ** 2
    print(works)
    return sum(works)

print(solution(9, [1, 1, 1]))