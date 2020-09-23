from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
Map = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
n, m  = len(Map), len(Map[0])

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if Map[nx][ny] == 0:
                continue
            
            if Map[nx][ny] == 1:
                Map[nx][ny] = Map[x][y] + 1
                queue.append((nx, ny))
                
    return Map[n-1][m-1]

print(bfs(0, 0), Map)
            