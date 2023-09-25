'''
입력: 첫 번째에 노드의 개수 n이 주어집니다.
이어지는 n개의 줄에 걸쳐 인접행렬에 대한 정보가 주어집니다.

출력: level 2에 도착할 때마다 탐색 경로를 출력합니다.

입력예시
9
0 1 1 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 1 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

출력예시
0 1 3
0 1 4
0 1 5
0 2 6
0 2 7
0 2 8
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
def dfs(n, arr, start):
    stack = [start]
    visited = [0] * 3
    level = 0
    while stack:
        now = start
        for next in range(1, n):
            if arr[now][next] and not visited[next]:
                stack.append[next]
                now = next
                visited[next] = True
                level += 1

            elif:
                stack.pop()

visited2 = [0] * 3
def DFS(now, level):
    global visited
    visited2[level] = str(now) # 현재 방문한 노드를 저장
    if level == 2: # 모든 노드를 방문했으면 -> 노드를 출력
        print(' '.join(visited2))
    for i in range(N):
        if arr[now][i] == 1:
            DFS(i, level + 1)

DFS(0,0)