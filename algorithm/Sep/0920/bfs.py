from collections import deque


k = int(input())
def bfs(now):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        print(now, end = ' ')
        for i in range(6):
            if arr[now][i] == 1:
                q.append(i)

bfs(0)