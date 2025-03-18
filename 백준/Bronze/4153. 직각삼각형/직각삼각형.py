while 1:
    li = list(map(int, input().split()))
    if li[0] == 0:
        exit()
    li.sort()
    if li[2] * li[2] == li[0] * li[0] + li[1] * li[1]:
        print("right")
    else:
        print("wrong")