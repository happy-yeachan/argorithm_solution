def solution(tickets):
    # 경로를 저장할 배열
    global road, check
    road = ["ICN"]
    check = [0]*len(tickets)
    # ICN부터 시작
    dfs("ICN", tickets)
    return road

def dfs(x, tickets):
    # 배열이 비었으면 끝
    if len(road) == len(tickets)+1:
        return

    tmp_i = 0
    tmp = 'ZZZZ'
    for i in range(len(tickets)):
        if check[i] == 0 and tickets[i][0] == x and tickets[i][1] < tmp:
            tmp = tickets[i][1]
            tmp_i = i
        # 다른 길을 찾았으면 막다른 길 다시 열어주기
    for i in range(len(check)):
        if check[i] == -1:
            check[i] = 0

    # 막다른 길이면 -1로 표시해서 막다른 길이라고 표시
    if tmp == 'ZZZZ':
        no = road.pop()
        check[check.index(max(check))] = -1
        dfs(road[-1],tickets)
    else:
        road.append(tmp)
        check[tmp_i] = len(road)-1
        dfs(tmp, tickets)