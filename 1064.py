def dis(i, j):
    return (((i[0] - j[0])**2 + (i[1] - j[1])**2)**(1/2))

a = [0, 0]
b = [0, 0]
c = [0, 0]
d = []
a[0], a[1], b[0], b[1], c[0], c[1] = input().split()
a = list(map(int, a))
b = list(map(int, b))
c = list(map(int, c))

if (a[0] == b[0] == c[0] or a[1] == b[1] == c[1]):
    print(-1)
    exit()
else:
    if((b[0] - a[0]) == 0):
        t1=(b[1]-a[1])
    elif((c[0] - a[0]) == 0):
        t2=(c[1]-a[1])
    else:
        t1 = (b[1]-a[1])/(b[0] - a[0])
        t2 = (c[1]-a[1])/(c[0] - a[0])
        if (t1 == t2):
            print(-1)
            exit()

d.append(dis(a, b))
d.append(dis(a, c))
d.append(dis(b, c))
d.sort()
print(((d[1]+d[2])*2)-((d[0]+d[1])*2))