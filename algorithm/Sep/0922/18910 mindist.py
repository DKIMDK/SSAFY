import heapq
#인접리스트
def dijkstra(start):
    dist[start] = 0
    for _ in range(N + 1):
        min_idx = -1
        min_value = float('inf')

        for i in range(N + 1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1

        for i in range(N+1):
            if arr[min_idx][i] and not visited[i]:
                dist[i] = min(dist[i], dist[min_idx] + arr[min_idx][i])


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    arr = [[0 for _ in range(N+1)] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    dist = [float('inf') for _ in range(N + 1)]

    for s, e, w in edges:
        arr[s][e] = w
    dijkstra(0)
    print(f'#{tc} {dist[N]}')
