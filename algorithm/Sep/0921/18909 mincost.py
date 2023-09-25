from collections import deque

def bfs(r, c):
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited[r][c] = 0
    que = deque()
    que.append((r, c))
    while que:
        r, c = que.popleft()
        for dr, dc in dir:
            nr, nc = r + dr, c + dc

            if 0 <= nr < N and 0 <= nc < N:
                val = 0
                # 1. 현재 지점보다 높은 지역으로 이동할 때 높이 차이 계산
                if arr[nr][nc] > arr[r][c]:
                    val = arr[nr][nc] - arr[r][c]
                # 2. 이동하려는 위치의 연료 소비량 갱신
                if visited[r][c] + 1 + val < visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1 + val
                    que.append((nr, nc))
    return visited[N-1][N-1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[float('inf')] * N for _ in range(N)]
    bfs(0,0)
    print(f'#{tc} {visited[N-1][N-1]}')