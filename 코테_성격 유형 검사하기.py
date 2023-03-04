def solution(survey, choices):
    li = [0 for i in range(100)]
    tmp = 0
    answer = ''
    for i in choices:
        if (i<4):li[ord(survey[tmp][0])] += (4-i)
        elif(i>4):li[ord(survey[tmp][1])] += (i-4)
        tmp +=1
    if (li[82] >= li[84]): answer += "R"
    else: answer += "T"
    if (li[67] >= li[70]): answer += "C"
    else: answer += "F"
    if (li[74] >= li[77]): answer += "J"
    else: answer += "M"
    if (li[65] >= li[78]): answer += "A"
    else: answer += "N"
    return answer
# RT CF JM AN
print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))