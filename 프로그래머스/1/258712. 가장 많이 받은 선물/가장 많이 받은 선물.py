def solution(friends, gifts):
    n = len(friends)
    name_to_idx = {name: idx for idx, name in enumerate(friends)}
    
    # 1. 주고받은 선물 기록
    gift_record = [[0]*n for _ in range(n)]
    gift_score = [0]*n  # 선물 지수
    
    for g in gifts:
        giver, receiver = g.split()
        gi, ri = name_to_idx[giver], name_to_idx[receiver]
        gift_record[gi][ri] += 1
        gift_score[gi] += 1
        gift_score[ri] -= 1

    # 2. 다음 달 받을 선물 수 계산
    next_month = [0]*n
    
    for i in range(n):
        for j in range(i+1, n):
            if gift_record[i][j] > gift_record[j][i]:
                next_month[i] += 1
            elif gift_record[i][j] < gift_record[j][i]:
                next_month[j] += 1
            else:
                if gift_score[i] > gift_score[j]:
                    next_month[i] += 1
                elif gift_score[i] < gift_score[j]:
                    next_month[j] += 1
                # 같으면 아무도 못 받음

    return max(next_month)
