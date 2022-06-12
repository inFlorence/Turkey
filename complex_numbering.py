# BAKEJOON-2667 
# https://www.acmicpc.net/problem/2667

import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_apt = [list(map(int,list(readl().strip()))) for r in range(N)]
	return N, map_apt   

size = 0
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

def Flood_Fill_DFS(r, c):
    global size
    map_apt[r][c] = 0
    size += 1
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if not 0 <= nr < N : continue
        if not 0 <= nc < N : continue
        if map_apt[nr][nc] == 0: continue
        Flood_Fill_DFS(nr, nc)
    
def Solve():
    global size
    list_size = []
    sys.setrecursionlimit(N*N)
    # 셀 각각 스캔 진행 
    for r in range(N): 
        for c in range(N):
            if map_apt[r][c] == 0: continue
            size = 0 # 재귀함수에서 size 를 증가시킴 
            Flood_Fill_DFS(r, c)
            list_size.append(size) # 해당 단지의 집의 개수
    list_size.sort()
    return list_size  
            
cnt = -1
list_size = []

# 입력 받는 부분
N, map_apt = Input_Data()

# 여기서부터 작성
list_size = Solve()
cnt = len(list_size)

# 출력하는 부분
print(cnt)
print(*list_size,sep='\n')