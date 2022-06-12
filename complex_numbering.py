import sys
from collections import deque
 
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_apt = [[0] + list(map(int,list(readl().strip()))) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N, map_apt
 
 
sys.setrecursionlimit(50 * 50) # Recursion 중첩 제한 설정
def Flood_Fill_DFS(r, c):
    global size
    size += 1
    map_apt[r][c] = 0
 
    for dr,dc in d:
        nr,nc = r+dr,c+dc
        if not 1 <= nr <= N: continue
        if not 1 <= nc <= N: continue
        if map_apt[nr][nc] == 0: continue
        Flood_Fill_DFS(nr, nc)
 
 
def Flood_Fill_BFS(r, c):
    global q
    q = deque()
    map_apt[r][c] = 0
    q.append((r, c))
    size = 1
    while q:
        r,c = q.popleft()
        for dr,dc in d:
            nr, nc = r+dr, c+dc
            if not 1 <= nr <= N: continue
            if not 1 <= nc <= N: continue
            if map_apt[nr][nc] == 0 : continue
            map_apt[nr][nc] = 0
            q.append((nr, nc))
            size += 1
    return size
 
 
def Solve():
    global size
    list_size = []
    for r in range(1,N+1):
        for c in range(1,N+1):
            if map_apt[r][c]:
                """
                # DFS 방식 Flood-Fill
                size = 0
                Flood_Fill_DFS(r, c) """
 
                # BFS 방식 Flood-Fill
                size = Flood_Fill_BFS(r, c)
                 
                list_size.append(size)
    list_size.sort()
    return len(list_size), list_size
 
 
# 입력 받는 부분
N, map_apt = Input_Data()
 
# 여기서부터 작성
size = 0
d = ((1,0),(-1,0),(0,1),(0,-1))
q = 0
cnt,list_size = Solve()
 
# 출력하는 부분
print(cnt)
print(*list_size,sep='\n')