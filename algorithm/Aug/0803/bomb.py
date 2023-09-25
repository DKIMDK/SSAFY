N, M = map(int, input().split())
b_range = int(input())
field = [list(input()) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


for i in range(N):
    for j in range(M):
        obj = field[i][j]
        if obj == '@':
            for k in range(4):
                for p in range(1, b_range+1):

                    ni = i + di[k] * p
                    nj = j + dj[k] * p

                    if 0 <= ni < N and 0 <= nj < M:
                        if field[ni][nj] == '#' or field[ni][nj] == '@':
                            break
                        field[ni][nj] = '%'
            field[i][j] = '%'

for row in field:
    print(*row, sep = '')
