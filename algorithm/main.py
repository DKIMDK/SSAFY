T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ## 10x 10 격자 생성
    arr = [[0]* 10 for _ in range(10)]
    result = 0
    for k in range(N):
        x1, y1, x2, y2, color = map(int, input().split())

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                arr[i][j] += color
                # 격자 값이 3이면 카운팅
                if arr[i][j] == 3:
                    result += 1
    print(f'#{tc} {result}')