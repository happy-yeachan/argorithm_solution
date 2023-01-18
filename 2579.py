#2579번

a = int(input())
sl= []
for _ in range(a):
    sl.append(int(input()))

#비교값 만들기
dp = []
dp.append(sl[0])
dp.append(sl[0] + sl[1])
dp.append(max(sl[0] + sl[2], sl[1] + sl[2]))
# 첫 계단+바로 다음 계단,  첫 계단 + 한칸 뛴 계단 둘 중 큰값 저장

#가중치 비교 (4번째 계단부터 시작)
for i in range(3, a):
    dp.append(max(dp[i - 2] + sl[i], dp[i - 3] + sl[i - 1] + sl[i]))

print(dp.pop())