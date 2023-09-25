
def find_p(N, M, arr):
    for i in range(N):
        for j in range(N - M + 1):
            h = arr[i][j: j + M]

            v = [arr[k][i] for k in range(j, j + M)]

            if h == h[::-1]:
                return h
            if v == v[::-1]:
                return v

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = find_p(N, M, arr)
    print(f'#{tc}', "".join(result))