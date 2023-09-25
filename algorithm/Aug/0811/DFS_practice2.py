'''
숫자 n과 인접행렬을 입력받습니다.
DFS를 돌리고, 탐색 순서대로 출력 해 주세요.

유의사항
노드 값은 없으며, 노드 번호를 출력
항상 0번부터 탐색 시작
자식 노드가 여러개라면 노드 번호가 작은 것부터 탐색
1 <= n <= 100
노드 번호는 0~ n-1

입력 예시
5
0 1 1 0 0
0 0 0 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

출력
0 1 3 4 2
'''

def dfs(n, adj, start):
    stack = [start]
    visited = [False] * n
    result = [start]
    while True:
        for now in range(1, n):
            if adj[now][now] and not visited[now]:
                stack.append(now)
                result.append(now)
                now = now
                visited[now] = True
                break
        else:
            if stack:
                stack.pop()
            else:
                break
    return result


def dfs2(n, adj, now):
    visited = [False] * n
    result = []

    def explore(now):
        visited[now] = True
        result.append(now)
        for next in range(n):
            if adj[now][next] and not visited[next]:
                explore(next)
    explore(now)
    return result


T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]

print(dfs2(T, arr, 0))