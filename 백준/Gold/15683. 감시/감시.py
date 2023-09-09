import sys
input = sys.stdin.readline

# 상하좌우 #으로 체우는 함수를 미리 만들어둠
def c1(tmp, p):
    for i in range(p[1], m):
        if tmp[p[0]][i] == 6:
            break
        elif tmp[p[0]][i] == 0:
            tmp[p[0]][i] = '#'
    return tmp

def c2(tmp, p):
    for i in range(p[0], n):
        if tmp[i][p[1]] == 6:
            break
        elif tmp[i][p[1]] == 0: 
            tmp[i][p[1]] = '#'
    return tmp

def c3(tmp, p):
    for i in range(p[1], -1, -1):
        if tmp[p[0]][i] == 6:
            break
        elif tmp[p[0]][i] == 0:
            tmp[p[0]][i] = '#'
    return tmp

def c4(tmp, p):
    for i in range(p[0], -1, -1):
        if tmp[i][p[1]] == 6:
            break
        if tmp[i][p[1]] == 0:
            tmp[i][p[1]] = '#'
    return tmp

# 각 카메라별 어떤 경우 사용할지 하는지 따로 저장한다.
def back(cnt):
    global result
    if cnt == len(cam):
        tmp_li = [mat[:] for mat in li]
        result = min(result, overlook(tmp_li))
        return

    elif li[cam[cnt][0]][cam[cnt][1]] == 1:
        for i in range(4):
            case.append((1,i))
            back(cnt+1)
            case.pop()
    elif li[cam[cnt][0]][cam[cnt][1]] == 2:
        for i in range(2):
            case.append((2,i))
            back(cnt+1)
            case.pop()
    elif li[cam[cnt][0]][cam[cnt][1]] == 3:
        for i in range(4):
            case.append((3,i))
            back(cnt+1)
            case.pop()
    elif li[cam[cnt][0]][cam[cnt][1]] == 4:
        for i in range(4):
            case.append((4,i))
            back(cnt+1)
            case.pop()
    elif li[cam[cnt][0]][cam[cnt][1]] == 5:
        case.append((5,0))
        back(cnt+1)
        case.pop()

# 카메라가 사용할 경우를 따져 감시를 한다고 가정하고 사각지대 탐색
def overlook(tmp_li):
    cnt = 0
    for i in range(len(case)):
        if case[i][0] == 1:
            tmp_li = case1[case[i][1]](tmp_li, cam[i])
        elif case[i][0] == 2:
            tmp_li = case2[case[i][1]][0](tmp_li, cam[i])
            tmp_li = case2[case[i][1]][1](tmp_li, cam[i])
        elif case[i][0] == 3:
            tmp_li = case3[case[i][1]][0](tmp_li, cam[i])
            tmp_li = case3[case[i][1]][1](tmp_li, cam[i])
        elif case[i][0] == 4:
            tmp_li = case4[case[i][1]][0](tmp_li, cam[i])
            tmp_li = case4[case[i][1]][2](tmp_li, cam[i])
            tmp_li = case4[case[i][1]][1](tmp_li, cam[i])
        elif case[i][0] == 5:
            tmp_li = c1(tmp_li, cam[i])
            tmp_li = c2(tmp_li, cam[i])
            tmp_li = c3(tmp_li, cam[i])
            tmp_li = c4(tmp_li, cam[i])        
    for i in range(n):
        for j in range(m):
            if tmp_li[i][j] == 0:
                cnt+=1
    return cnt

case1 = [c1, c2, c3, c4]
case2 = [[c1,c3], [c2,c4]]
case3 = [[c1,c2],[c2,c3],[c3,c4],[c4,c1]]
case4 = [[c1,c2,c3],[c2,c3,c4],[c3,c4,c1],[c4,c1,c2]]



n, m = list(map(int,input().split()))
li = [list(map(int,input().split())) for _ in range(n)]
case = []
cam = []
result = 64
for i in range(n):
    for j in range(m):
        if li[i][j] != 0 and li[i][j] != 6:
            cam.append((i,j))

back(0)
print(result)