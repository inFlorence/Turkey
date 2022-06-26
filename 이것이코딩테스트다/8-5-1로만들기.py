# 다이나믹 프로그래밍 풀기
#
# 1. 완전 탐색 알고리즘으로 접근했을 때, 시간이 매우 오래 걸리는 경우 
# 2. 해결하고자 하는 부분 문제들의 중복여부 확인 
# 3-1. 단순히 재귀 함수로 비효율적인 프로그램을 작성한 뒤 (top-down) -> sys.setrecursionlimit 
# 3-2. 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있으면, memoization 적용
# 3-2. bottom-up 방식으로 구현 

# 1 로 만들기 
# https://www.acmicpc.net/problem/1463
# ai = min(ai-1, ai/2, ai/3, ai/5) + 1

def DP_bottom_up(x):
    # DP 테이블 초기화 
    d = [0] * 30001
    
    # 1번 규칙 (5으로 나누어 떨어진다) : D[N] = D[N/5] + 1
    # 2번 규칙 (3으로 나누어 떨어진다) : D[N] = D[N/3] + 1
    # 3번 규칙 (2로 나누어 떨어진다) : D[N] = D[N/2] + 1
    # 4번 규칙 ( 1 을 뺀다 ): D[N] = D[N-1] + 1
    for i in range(2, x+1):
        d[i] = d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i % 3 == 0:
            d[i] == min(d[i], d[i//3]+1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5]+1)
    return d[x]

x = int(input())
print(DP_bottom_up(x))
# print(DP(x)) # wrong answer