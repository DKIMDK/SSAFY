import heapq
n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
dist = [[float('inf')] * m for _ in range(n)]

ydir = [0, 0, 1, -1]
xdir = [-1, 1, 0, 0]

def dijkstra():
    pq = []
    dist[0][0] = MAP[0][0]
    heapq.heappush(pq, (MAP[0][0], 0, 0))
    while pq:
        cost, y, x = heapq.heappop(pq)

        # 이미 확인 한 좌표일 경우 (더 짧은 경로를 발견한 경우)
        if dist[y][x] < cost:
            continue

        for i in range(4):
            ny = y + ydir[i]
            nx = x + xdir[i]
            # 맵 범위를 벗어나면
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            nextcost = cost + MAP[ny][nx]   # 다음 지점까지의 거리
            # 이미 발견한 경우가 더 짧은 경우 continue
            if dist[ny][nx] <= nextcost:
                continue
            dist[ny][nx] = nextcost # 최단거리 distance 갱신
            heapq.heappush(pq, (nextcost, ny, nx))  #우선순위 큐에 다음 지점 정보 넣기
    return dist[n-1][m-1]   # 최단거리 반환

print(dijkstra())
