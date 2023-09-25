from collections import deque
dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    check = [[-1 for _ in range(M)] for _ in range(N)]  # 최단 거리를 저장할 리스트
    q = deque()

    for i in range(N):
        t = input() # 격자를 입력 받으면서
        for j in range(M):
            if t[j] == 'W': # W를 발견하면
                q.append((i, j))    # 큐에 추가 후
                check[i][j] = 0     # 거리를 0으로 설정
    result = 0
    while q:
        x, y = q.popleft()  # 큐에서 하나를 꺼내고, 상하 좌우로 이동
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            # 이동 가능, 아직 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == -1:
                q.append((nx, ny))                  # 큐에 추가
                check[nx][ny] = check[x][y] + 1     # 거리 갱신
                result += check[nx][ny]             # result 갱신
    print(f'#{tc} {result}')