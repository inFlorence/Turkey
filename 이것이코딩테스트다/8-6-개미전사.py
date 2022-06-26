# 8-6. 3.개미전사
# 
# 입력조건 
# - 첫째 줄에 식량창고의 개수 N이 주어진다 (3 <= N <= 100)
# - 둘째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다 (0 <= K <= 1000)
# 출력조건
# - 첫째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오

# 정수 N 을 입력받기 
n = int(input())
# 모든 식량정보 K개 입력받기 
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화 
d = [0] * 100

# Dynamic Programming (Bottom-up)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])