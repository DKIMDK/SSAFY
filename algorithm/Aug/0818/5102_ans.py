from collections import deque
def bfs(start, end):
    queue = deque([(start, 0)])         # 큐에 시작노드와, 초기거리 0을 넣기
    while queue:
        n, cnt = queue.popleft()        # 현재 노드와, 거리 디큐

        if not visited[n]:              # 노드 방문하지 않았다면
            visited[n] = 1              # 방문 표시

        for j in arr[n]:
            if not visited[j] and j == end: # 목표 노드에 도착
                return cnt + 1              # 거리 + 1을 반환
            elif not visited[j]:            # 아직 방문하지 않은 노드
                queue.append((j, cnt + 1))
    return 0                                # 경로가 없으면 0 반환
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)] # 인접행렬 초기화
    visited = [0] * (V+1)
    for i in range(E):
        n1, n2 = map(int, input().split())
        arr[n1].append(n2)
        arr[n2].append(n1)
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S, G)}')