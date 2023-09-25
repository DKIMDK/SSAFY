T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    max_area = 0 # 최대면적
    cnt = 0

    for y in range(N):
        for x in range(N):
            cur = MAP[y][x] # 현재 위치

            for ny in range(y, N):
                for nx in range(x, N):

                    if MAP[ny][nx] == cur:
                        area = (ny - y + 1) * (nx - x + 1)

                        if max_area < area:
                            max_area = area
                            cnt = 1
                        elif area == max_area:
                            cnt += 1
