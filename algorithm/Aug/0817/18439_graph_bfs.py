arr =[
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0]
]
from collections import deque
start = int(input())
queue = [0]
visited = [0] * 6
def bfs(now):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        print(now)
        for i in range(6):
            if visited[i] == 1: continue
            if arr[now][i] == 1:
                visited[i] = 1
                q.append(i)

visited[start] = 1
# bfs(start)