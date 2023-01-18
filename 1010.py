def com(x, y):
    up = 1
    down = 1
    for a in range(y):
        up *= (x-a)
        down *= a+1
    return(int(up/down))

i=int(input())
idk = []
for k in range(i):
    a, b = input().split()
    idk.append(com(int(b),int(a)))

for a in idk:
    print(a)