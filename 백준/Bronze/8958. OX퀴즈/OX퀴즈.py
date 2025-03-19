T = int(input())

for i in range(T):
    test = input()
    start = 1
    result = 0
    for i in range(len(test)):
        if test[i] == "O":
            result += start
            start += 1
        else:
            start = 1
    print(result)