def check(arr):
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            row[arr[i][j]] += 1
            if row[arr[i][j]] >= 2:
                return 0

            col[arr[j][i]] += 1
            if col[arr[j][i]] >= 2:
                return 0

        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                matrix = [0] * 10
                for i in range(3):
                    for j in range(3):
                        matrix[arr[y+i][x+j]] += 1
                        if matrix[arr[y+i][x+j]] >= 2:
                            return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {check(arr)}')