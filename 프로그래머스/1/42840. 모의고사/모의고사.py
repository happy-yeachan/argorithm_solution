def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]

    for i, ans in enumerate(answers):
        if ans == p1[i % len(p1)]: scores[0] += 1
        if ans == p2[i % len(p2)]: scores[1] += 1
        if ans == p3[i % len(p3)]: scores[2] += 1

    max_score = max(scores)
    return [i+1 for i, s in enumerate(scores) if s == max_score]