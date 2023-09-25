'''
아래 그래프에는 이동 경로마다 기차 비용이 적혀있습니다.
출발 지점에서 도착지점까지 가장 저렴한 방법으로 이동하려고 합니다.
,가장 저렴한 노선의 비용을 알려주는 프로그램을 제작해 주세요.

입력
첫 줄에는 정점의 개수 N과 간선의 수 T를 입력 받습니다. (1 <= N <= 20,000 , 1 <= T <= 300,000)

모든 정점에는 0번 부터 N-1번까지 번호가 매겨져 있다고 가정합니다.
둘째 줄부터 T 개의 노선 정보를 입력 받는데, 각 줄마다 3개의 정수 (a, b, w)로 입력 받습니다. ( a와 b는 서로 다르며, 1 <= w <= 10,000 의 자연수)
이는 시간이 w 만큼 걸리는 a 에서 b 로 가는 간선이 존재한다는 뜻입니다.

예를들어 0 2 4 인경우 0번에서 2번 노드까지 도착하는데 걸리는 시간은 4 입니다.

출력
0번 노드에서 출발하여 N - 1 노드에 도착해야 합니다.
이때, 가장 저렴하게 갈수 있는 비용을 출력해 주세요.
만약 갈수 있는 길이 없다면, "impossible" 을 출력합니다.
'''

import heapq
N, T = map(int, input().split())
graph = [[] for i in range(N)]
for _ in range(T):
    a, b, w = map(int, input().split())
    graph[a].append([b, w])

INF = float('inf')
distance = [INF] * N

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:

        dist, now = heapq.heappop(pq)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

dijkstra(0)

if distance[N-1] == INF:
    print('impossible')
else:
    print(distance[N-1])
