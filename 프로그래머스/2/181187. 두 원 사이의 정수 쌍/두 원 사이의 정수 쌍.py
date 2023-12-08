def solution(r1, r2):
    r1_point, dup_point = get_point(r1)
    r2_point, tmp = get_point(r2)
    answer = r2_point - r1_point + dup_point
    return answer

def get_point(r):
    p = 0
    dup_point = 0
    for i in range(r):
        p += int((r**2 - i**2)**(1/2))
        if ((r**2 - i**2)**(1/2))%1 == 0:
            dup_point +=1
    dup_point *= 4
    p *=4
    p += 1
    return p, dup_point