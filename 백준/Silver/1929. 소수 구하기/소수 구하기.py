M, N = map(int, input().split())

result = []

for num in range(M, N + 1):
    if num > 1:  # 1은 소수가 아니므로 제외
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  # 제곱근까지만 검사
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)

for i in result:
    print(i)
