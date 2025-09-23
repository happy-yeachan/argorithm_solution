
def solution(clothes):
    answer = 1
    dic = {}
    for name, types in clothes:
        if types in dic:
            dic[types] += 1
        else:
            dic[types] = 1
    
    for i in dic:
        answer *= (dic[i] + 1)
    
    return answer -1