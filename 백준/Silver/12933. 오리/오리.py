# q가 나오면 li에 추가하여 오리 추적 시작
# q가 아닌 문자가 나오면 li 중
# 현재 문자가 해당 오리에게 올 차례인지 확인
# 맞는 오리를 찾아 해당 문자 추가
# 오리 울음이 완료되면 해당 오리를 ("")로 처리
# 문자를 넣을 수 있는 오리를 못 찾았는데 그 문자가 q가 아니면 -1 반환
# 모든 문자를 순회하며 동시에 울고 있는 오리 수를 추적하고 그 최대값 저장

sound = list(input())

li = []  # 각 오리의 울음 진행 상태를 저장하는 리스트
max_cnt = 0

for tmp in sound:
    
    placed = False
    for j in range(len(li)):
        now = li[j]
        expected = "quack"[len(now)]  # 현재 오리가 기대하는 다음 문자
        if tmp == expected:
            li[j] += tmp
            if li[j] == "quack":  # 오리 울음 완성 시 초기화
                li[j] = ""
            placed = True
            break

    # 어떤 오리에도 넣지 못했다면 잘못된 순서
    if not placed:
        if tmp == "q":
            li.append("q")
            placed = True
        else:
            print(-1)
            exit()

    # 현재 울고 있는 오리 수 세기
    current = 0
    for duck in li:
        if duck != "":
            current += 1
    max_cnt = max(max_cnt, current)

# 모든 오리가 울음을 끝냈는지 확인
for duck in li:
    if duck != "":
        print(-1)
        exit()

print(max_cnt)
