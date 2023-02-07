#코테_타겟넘버
#DFS/BFS

from itertools import combinations
def solution(numbers, target):
    cnt = 0
    for i in range(1, len(numbers)+1):
        li = list(combinations(numbers, i))  #1, 2, 3 ...개를 뽑아서 그 뽑은 수들을 -를 붙여서 계산해보기
        for j in li:
            if (sum(numbers)-(2*sum(list(j))) == target):  #뽑은 수를 빼야하니까 전체를 더한 값에서 뽑은 수를 2번빼주면 됨
                cnt += 1

    return cnt


print(solution([4, 1, 2, 1], 4))