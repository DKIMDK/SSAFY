dir1 = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dir2 = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
T = int(input())
for tc in range(1, T+1):
    best_kill = 0
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            total1 = arr[y][x]
            total2 = arr[y][x]
            for dy, dx in dir1:
                for k in range(1, M):
                    ny, nx = y + dy * k, x + dx * k
                    if 0 <= nx < N and 0 <= ny < N:
                        total1 += arr[y][x]
            best_kill = max(total1, best_kill)
            for dy, dx in dir2:
                for k in range(1, M):
                    ny, nx = y + dy * k, x + dx * k
                    if 0 <= nx < N and 0 <= ny < N:
                        total2 += arr[y][x]
            best_kill = max(total2, best_kill)

    print(best_kill)