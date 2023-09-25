'''
민철이는 A도시로부터 B도시로까지 물품을 운송하는 화물 기사입니다.
운송을 완료하기 위해서는 여러 고속도로를 거쳐야 하는데,
이에 지불하는 통행료는 사비로 해결해야 하기 때문에,
항상 최소한의 비용으로 이동할 수 있는 경로를 선택합니다.
하지만 새로운 정부의 통행료 정책에 의해, 매년 고속도로의 통행료가 일괄적으로 물가상승률에 맞춰 인상됩니다.

도시와 고속도로의 정보, A도시와 B도시, 그리고 각 해의 물가상승률이 주어졌을 때,
민철이가 각 해에 지불해야 하는 A도시로부터 B도시까지의 최소 통행료를 출력하는 프로그램을 작성하세요.

입력
첫 번째 줄에 도시의 수 N (2 ≤ N ≤ 1,000), 고속도로의 수 M (1 ≤ M ≤ 30,000),
그리고 햇수 K (0 ≤ K ≤ 30,000)가 주어집니다.
두 번째 줄에는 도시 A와 도시 B (1 ≤ A, B ≤ N, A ≠ B)가 주어집니다.
도시 번호는 1번부터 시작합니다.
다음 M개의 줄에는 각각 도로 정보를 나타내는 세 정수
f, t (1 ≤ f < t ≤ N), c (1 ≤ c ≤ 1,000)가 주어집니다.
도시 f와 도시 t가 통행료 c인 도로로 연결되어 있다는 것을 의미합니다.
다음 총 K개의 줄에는 각각 정수 p (1 ≤ p ≤ 10)가 주어진다.
각각 1년후, 2년후, ... , K년 후 인상되는 금액을 의미합니다.
A에서 B로 이동할 수 없는 경우는 주어지지 않습니다.

출력
첫 번째 줄에 첫 해의 최소 통행료를 출력합니다.
두 번째 줄부터 K개의 줄에 각각 1년 후, 2년 후 ... , K년 후에
세금이 올랐을 때의 최소 통행료를 출력합니다.

'''
import heapq

def min_toll(graph, start, end):
    N = len(graph)
    min_tolls = [float('inf')] * N
    min_tolls[start] = 0
    pq = [(0, start)]

    while pq:
        cost, current_city = heapq.heappop(pq)

        if cost > min_tolls[current_city]:
            continue

        for next_city, next_cost in graph[current_city]:
            if cost + next_cost < min_tolls[next_city]:
                min_tolls[next_city] = cost + next_cost
                heapq.heappush(pq, (cost + next_cost, next_city))

    return min_tolls[end]

N, M, K = map(int, input().split())
A, B = map(int, input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    f, t, c = map(int, input().split())
    graph[f-1].append((t-1, c))
    graph[t-1].append((f-1, c))

# 첫 해
print(min_toll(graph, A-1, B-1))

# 다음 해
for _ in range(K):
    p = int(input())
    for i in range(N):
        for j in range(len(graph[i])):
            graph[i][j] = (graph[i][j][0], graph[i][j][1] + p)
    min_toll_k = min_toll(graph, A-1, B-1)
    print(min_toll_k)
