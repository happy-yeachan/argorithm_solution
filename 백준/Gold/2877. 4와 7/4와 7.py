K = int(input())

length = 1
count = 0

# 몇자리인지 판단
while True:
    num_count = 2 ** length
    if count + num_count >= K:
        break
    count += num_count
    length += 1

# 그 자리수에서 몇번째인지 확인
index = K - count - 1

# 위 값 기반 2진수 생성
binary = bin(index)[2:].zfill(length)

# 0을 4로 1을 7로 변환
result = ''
for i in binary:
    if i == '0':
        result += '4'
    else:
        result += '7'

print(result)
