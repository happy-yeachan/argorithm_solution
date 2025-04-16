N = int(input())

for i in range(N):
    password = input()
    if len(password) < 6 or len(password) > 9:
        print("no")
    else:
        print("yes")