# 4. 바닥공사

# input condition
# - 첫째 줄에 N이 주어진다 (1<=N<=1000)
# output condition 
# - 첫째 줄에 2xN 크기의 바닥을 채우는 방법의 수를 796,796 으로 나눈 나머지를 출력한다. 

# 정수 N을 입력받기 
n = int(input())
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# Dynamic progammin (Bottom-up)
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]*2) % 796796

print(d[n])