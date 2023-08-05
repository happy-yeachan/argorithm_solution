from collections import deque


def solution(begin, target, words):
    w_len = len(begin)
    w_cnt = len(words)
    cnt = [0]*(len(words))
    # words에 target이 없으면 0반환
    if target not in words:
        return 0
    q = deque([])
    for i in range(w_cnt):
        tmp = 0
        for j in range(w_len):
            if begin[j] != words[i][j]:
                tmp += 1
        if tmp == 1:
            q.append(i)
            cnt[i] += 1

    while q:
        now = q.popleft()
        if words[now] == target:
            return(cnt[now])
        else:
            for i in range(w_cnt):
                if cnt[i] == 0:
                    tmp = 0
                    for j in range(w_len):
                        if words[now][j] != words[i][j]:
                            tmp += 1
                    if tmp == 1:
                        q.append(i)
                        cnt[i] = cnt[now] +1
                
    return 0