# 코테_귤 고르기
# 최빈값 구해서 빼고 리스트 제 정의하고 반복하면 될듯?


# def solution(k, tangerine):
#     answer = 0
#     while(k>0):
#         m = max(tangerine, key=tangerine.count) #최빈값 추출
#         cnt = tangerine.count(m)
#         k -= cnt
#         tangerine = [i for i in tangerine if i != m] #컴프리핸션을 이용해 특정 요소 제거거
#         answer +=1
#     return answer
#시간초과 나온다;;

from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    lst = [list(i) for i in list(count.items())]
    lst.sort(key=lambda x: x[1], reverse=True)
    answer = 0
    for l in lst:
        value = l[1]
        if value>=k:
            answer += 1
            break
        else:
            k -= value
            answer += 1
    return answer
            


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))