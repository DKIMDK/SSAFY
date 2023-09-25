direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]
            for x, y in direction:
                for p in range(1, arr[i][j]+1):
                    dx, dy = i + x * p, j + y * p
                    if 0 <= dx < N and 0 <= dy < M:
                        cnt += arr[dx][dy]
            if max_v < cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')