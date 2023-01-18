from itertools import combinations

def solution(orders, course):
    test = []
    for i in course:
        idk = []
        for j in orders:
            if i > len(max(set(orders), key=len)):   #course가 주문 최대 개수보다 큰 경우 무시1
                break
            idk += (list(combinations(list(sorted(j)), i)))    #조합을 이용해 course만큼 뽑는 모든 경우 구함, WX XW가 같은 경우인 것을 계산하기 위해 미리 정렬함
        
        try:    #course가 주문 최대 개수보다 큰 경우 무시2
            max_cnt = max(set(idk), key=idk.count)       #가장 많이 나오는 경우 찾기
            b = idk.count(max_cnt)
            if b != 1: # 2명 이상이 주문해야 하니까 1번 주문되었는지 확인
                test.append(''.join(max_cnt))   #리스트 요소들로 나누었던 값들을 문자열로 합쳐주는 작업
            idk.remove(max_cnt)
            
            for a in range(len(idk)):      #가장 많이 나오는 경우가 여러개일 경우 판별
                max_cnt = max(set(idk), key=idk.count)
                if  (idk.count(max_cnt) == b and idk.count(max_cnt) != 1):
                    test.append(''.join(max_cnt))
                    idk.remove(max_cnt)
                else:
                    break

        except:     #course가 주문 최대 개수보다 큰 경우 무시3
            continue

    
    return sorted(test) #사전순 정렬