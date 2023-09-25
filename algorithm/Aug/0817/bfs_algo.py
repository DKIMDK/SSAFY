def bfs(G, v):       # G: graph, v: starting point
    n = 10
    visited = [0] * (n + 1)     # n : 정점의 개수
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop(0)
        if not visited[t]:
            visited[t] = True
            print(t)                    # 정점 t에서 할 일
            for i in G[t]:
                if not visited[i]:
                    queue.append(i)