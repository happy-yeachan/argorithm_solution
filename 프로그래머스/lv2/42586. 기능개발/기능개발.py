def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0 
    
    while progresses:
        if (progresses[0] + time*speeds[0]) >=100 :  # 개발 완료
            progresses.pop(0)
            speeds.pop(0)
            count +=1 
            
        else : # 개발 덜 됨
            if count > 0 : # 연속으로 안 될 때
                answer.append(count) 
                count = 0
            time += 1
            
    answer.append(count)
    return answer