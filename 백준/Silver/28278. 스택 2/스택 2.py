from sys import stdin

input = stdin.readline

N = int(input())


# 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
# 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
# 3: 스택에 들어있는 정수의 개수를 출력한다.
# 4: 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.

li = []

for i in range(N):
    tmp = list(map(int, input().split()))

    if tmp[0] == 1:
        li.append(tmp[1])
    elif tmp[0] == 2:
        if len(li) >= 1:
            print(li.pop())
        else:
            print(-1)
    elif tmp[0] == 3:
        print(len(li))
    elif tmp[0] == 4:
        if len(li) >= 1:
            print(0)
        else:
            print(1)
    else:
        if len(li) >= 1:
            print(li[-1])
        else:
            print(-1)