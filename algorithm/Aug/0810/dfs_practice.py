def solution(start, end, adj):
    stack = []                                                   # path를 저장할 stack
    visited = [False] * (V + 1)                                 # 노드를 방문했는지를 0, 1로 표현
    stack.append(start)                                         # 시작점을 stack에 넣음
    while stack:                                                    # 스택이 비어있으면 반복문 종료
        now = stack.pop()                                       # 스택의 마지막 노드를 꺼냄
        visited[now] = True                                     # 현재 노드를 방문
        for next in range(1, V + 1):
            if adj[now][next] and not visited[next]:            # 방문하지 않았고, 연결되어 있다면
                stack.append(next)
    if visited[end]:                                            # 끝 점에 방문했다면
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        start, end = map(int, input().split())
        node[start][end] = 1
    S, G = map(int, input().split())
    print(f'#{tc} {solution(S, G, node)}')
    # arr = [map(int, input().split()) for _ in range(E)]
    # start, end = map(int, input().split())
    # adj_m = [[0] * (V+1) for _ in range(V+1)]
    # result = solution(start,end, V, adj_m)
    # print(f'#{tc} {result}')
