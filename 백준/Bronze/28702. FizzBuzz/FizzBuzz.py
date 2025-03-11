
li = []
ex = ['Fizz', 'Buzz', 'FizzBuzz']
for i in range(3):
    tmp = input()
    li.append(tmp)
    if tmp in ex:
        continue
    num = int(tmp)
    idx = i

result = num + 3 - idx

if result % 3 == 0 and result% 5 == 0:
    print("FizzBuzz")
elif result % 3 == 0:
    print("Fizz")
elif result % 5 == 0:
    print("Buzz")
else:
    print(result)