num = 64
a = int(input())
count = 0
if(num == a):
    print(1)
else:
    for i in range(6):
        num /= 2
        a -= num
        if(a == 0):
            break
