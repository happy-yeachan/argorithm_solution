def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    else:
        a = s//n
        b = s%n
        for i in range(n):
                answer.append(a)
        if b!=0:
            for i in range(b):
                answer[i] += 1
        answer.reverse()
    return answer