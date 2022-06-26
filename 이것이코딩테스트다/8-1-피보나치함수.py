def fibo(x):
    print('f(' + str(x) + ')', end=' ')
    # 종료 조건 (1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2) 

d = [0] * 100
def fibo_memoization(x): # Top-Down
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식을 따라서 피보나치 결과 반환 
    d[x] = fibo_memoization(x-1) + fibo_memoization(x-2)
    return d[x]
    
def fibo_memoization_bottom_up(x):
    b = [0] * 100 # DP 테이블
    b[1] = 1
    b[2] = 1
    # 피보나치 함수(Fibonacci Function) 반복문으로 구현 (Bottom-up Dynamic Programming)
    for i in range(3, x+1):
        b[i] = b[i-1] + b[i-2]
    print(b[x])
    
print(fibo(6))
print(fibo_memoization(6))
print(fibo_memoization_bottom_up(6))