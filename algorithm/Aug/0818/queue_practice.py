def bfs(s, V):
    visited = [0] * (V + 1)
    q = []
    visited[s] = 1  # 시작점 방문표시
    while q:  # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)  # 디큐
        print(t)  # 방문한 정점에서 할일
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)  # w 인큐
                visited[w] = visited[t] + 1


V, E = map(int, input().split())  # 1번부터 v번 정점, e개의 간선
arr = list(map(int, input().split()))
'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7

'''
# 인접리스트
adj_l = [[] for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
