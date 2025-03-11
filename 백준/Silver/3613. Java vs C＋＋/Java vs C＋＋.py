tmp = input()
result = "Error!"
cnt = tmp.count("_")
if "_" in tmp and tmp[0] != "_" and tmp[-1] != "_" and not any(char.isupper() for char in tmp):
    words = list(filter(None, tmp.split("_")))
    if len(words) > cnt:
        result=""
        result = words[0] + "".join(word.capitalize() for word in words[1:]) 

elif tmp[0].islower() and "_" not in tmp:
    result = ""
    result += tmp[0]
    for i in range(1, len(tmp)):
        if tmp[i].isupper():
            result += "_" + tmp[i].lower()
        else:
            result += tmp[i]

print(result)
