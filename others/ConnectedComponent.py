iceMap = [[0, 0, 1], [0, 1, 0], [1, 0, 1]]
n, m = len(iceMap), len(iceMap[0])

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if iceMap[x][y] == 0:
        iceMap[x][y] = 1
        # 상하좌우 노드 체크 (연결된 노드가 상하좌우라는 것을 알고 있기 때문에 따로 인접리스트를 생성할 필요가 없다)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        result += dfs(i, j)
        
print(result)
