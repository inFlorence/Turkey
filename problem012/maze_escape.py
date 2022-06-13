import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split()) # 4 <= N, M <= 200
    map_maze = [[0] + list(readl().split()) + [0] if 1<=r<=N else [0]*(N*2) for r in range(N+2)]
    return N, M, map_maze

def Solve_BFS():
    q = deque()
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    
    q.append((1, 1, 1))

    while q:
        r, c, dist = q.popleft()
        for dr, dc in d:
            nr, nc, ndist = r + dr, c + dc, dist + 1
            if not 1 <= nr <= N: continue
            if not 1 <= nc <= M: continue
            if int(map_maze[nr][nc]) == 0: continue
            if int(map_maze[nr][nc]) == 1: 
                map_maze[nr][nc] = ndist
                q.append((nr, nc, ndist))
    return map_maze[N][M]

sol = -1
N, M, map_maze = Input_Data()

sol = Solve_BFS()

print(sol)
 