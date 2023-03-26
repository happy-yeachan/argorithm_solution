# 코테_점프와 순간이동
# 점프는 1칸만하고 순간이동을 많이 쓰는게 가장 효율적
# 끝에서 뒤로 가는 방향으로 탐색

def solution(n):
    cnt = 1
    while(n!=1):
        if n%2 == 0:
            n /= 2
        else:
            n = (n-1)/2
            cnt += 1
    return cnt


print(solution(5))