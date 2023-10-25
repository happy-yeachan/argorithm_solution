import sys
from collections import deque
 
 
input_func = sys.stdin.readline
if __name__ == '__main__':
    N = int(*map(int, input_func().split()))
    #기다리는 줄, 입장 순서 리스트 생성
    waitings, entrance_order = deque(), []
    for _ in range(N):
        waiting_people = list(map(str, input_func().split()))
        #split으로 구역, 번호 분리 후 임시 덱 생성 
        temp_waitings = deque()
        for wp in waiting_people:
            space, number = wp.split('-')
            temp_waitings.append((space, int(number)))
        #기다리는 줄은 덱 그대로, 입장 순서 리스트에는 리스트로
        waitings.append(temp_waitings)
        entrance_order.append(list(temp_waitings))
    
    #(구역, 번호)데이터 sorting 후 deque 자료형
    entrance_order = deque(sorted(sum(entrance_order, [])))
    
    #콘서트 입장
    temp = []
    while entrance_order:   #입장할 티켓만큼 반복
        
        #현재 입장해야 하는 티켓
        person = entrance_order[0]
        
        #기다리는 줄 사람 확인
        if waitings and waitings[0] and person == waitings[0][0]:
            entrance_order.popleft()
            waitings[0].popleft()
        
        #대기 공간 사람 확인
        elif temp and person == temp[-1]:
            temp.pop()
            entrance_order.popleft()
        
        #입장해야 하는 티켓이 기다리는 줄과 대기 공간에 없는 경우
        else:
            #기다리는 사람이 없을 때, 더 이상 사람을 옮겨 줄 수 없으므로 종료
            if not waitings:
                break
            #기다리는 줄 사람을 대기공간으로 이동
            temp.append(waitings[0].popleft())
        
        #초기 기다리는 줄이 두 줄 이상이고, 현재 가장 앞 줄이 비어 있는 경우 
        if waitings and not waitings[0] and N >= 2:
            waitings.popleft()
 
    #모든 티켓이 입장했으면 GOOD
    if not entrance_order:
        print('GOOD')
    #입장하지 못한 티켓이 있으면 BAD
    else:
        print('BAD')
