# 8-5. 효율적인 화폐구성 

# input condition
# - 첫째 줄에 N, M이 주어진다 (1<=N<=100, 1<=M<=10000)
# - 이후 N개의 줄에 각 화폐의 가치가 주어진다. 화폐 가치는 10000보다 작거나 같은 자연수이다.
# output condition
# - 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
# - 불가능할 때는 -1을 출력한다.

# 정수 N, M 입력받기
N, M = map(int, input().split())
# N 개의 화폐단위 입력 받기 
array=[]
for _ in range(N):
    array.append(int(input()))

array.sort()

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화 
d = [10001] * (M+1)

# Dynamic Programing (Bottom-up)
d[0] = 0
for i in range(N):
    for j in range(array[i], M+1):
        if d[j-array[i]] != 10001 : # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]]+1)
            
if d[M] == 10001: # 최종적으로, M원을 만드는 방법이 없는 경우 
    print(-1)
else:
    print(d[M])