def solution(arr):
    N = len(arr)
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                stack.append([i, j])
                while stack:
                    y, x = stack.pop()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N:
                            if arr[ny][nx] == '3':
                                return 1
                            elif arr[ny][nx] == '0':
                                arr[ny][nx] = '-1'
                                stack.append([ny, nx])
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = solution(arr)
    print(f'#{tc} {ans}')
