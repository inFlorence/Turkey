import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    map_drinks = [[1] + list(map(int,list(readl().strip()))) + [1] if 1<=r<=N else [1]*(N+2) for r in range(N+2)]
    return N, M, map_drinks

d = ((-1, 0), (1, 0), (0, -1), (0, 1))

def Flood_Fill_DFS(r, c):
    map_drinks[r][c] = 1
    for dr, dc in d:
        nr, nc = r + dr, c + dc 
        if not 1 <= nr <= N : continue 
        if not 1 <= nc <= M : continue
        if map_drinks[nr][nc]: continue
        Flood_Fill_DFS(nr, nc)
        
def Flood_Fill_BFS(r, c):
    map_drinks[r][c] = 1

    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if not 1 <= nr <= N : continue
            if not 1 <= nc <= M : continue
            if map_drinks[nr][nc]: continue
            map_drinks[nr][nc] = 1
            q.append((nr, nc))
            
def Solve():
    cnt = 0
    #print(map_drinks)
    for r in range(1, N+1):
        for c in range(1, M+1):
            if map_drinks[r][c] == 0:
                """
                Flood_Fill_DFS(r, c)
                """
                Flood_Fill_BFS(r, c)
                cnt += 1
    return cnt

N, M, map_drinks = Input_Data()

sol = Solve()
print(sol)