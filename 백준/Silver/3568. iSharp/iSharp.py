li = input().split()

fix = li.pop(0)
for i in li:
    result = fix
    for j in range(len(i)-2, -1, -1):
        if i[j] == "*" or i[j] == "&":
            result += i[j]
        elif i[j] == "]":
            result += "[]"
        elif i[j] == "[":
            continue
        else:
            name = i[:j+1]
            break
    print (result, name + ";")