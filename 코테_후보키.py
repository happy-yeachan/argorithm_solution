from itertools import combinations


def solution(relation):
    answer = 0
    for j in range(1, len(relation[0])+1):
        combi = []
        for a in range(len(relation)):
            combi.append(list(combinations(relation[a], j)))
        tmp = list(map(list, zip(*combi)))
        print(tmp)
        
        for i in range(len(tmp)):
            if(len(tmp[i]) != len(set(tmp[i]))):
                continue
            else:
                answer += 1
                del relation[i]
        print(answer)

    return answer

# 하나로 중복 확인
# 중복이 되지 않은 요소 삭제 -> answer ++
# 콤비네이션 이용해서 2개씩 묶어주고 리스트 생성
# 중복 확인 중복 


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))