m = [
    [3, 3, 5, 3, 1],
    [2, 2, 4, 2, 6],
    [4, 9, 2, 3, 4],
    [1, 1, 1, 1, 1],
    [3, 3, 5, 9, 2]
    ]
''' 
map에서 대각선 방향의 합이 가장 큰 값이 나오는 좌표(y,x) 출력
대각선 합 구하는 함수를 만들어 사용
'''




di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

max_v = 0

for i in range(5):
    for j in range(5):
        # arr[i][j] 중심으로
        s = m[i][j]
        for k in range(4):
           #for p in range(1, m): ## 상하좌우 한 칸이 아니고 m칸을 search
            mi = i + di[k]*p
            mj = j + dj[k]*p
            if 0 <= mi < 5 and 0 <= mj < 5: ## 유효한 인덱스면, 가장자리에 있을 경우 오류 남을 방지
                 s += (m[mi][mj])
            # 여기까지 주변 원소를 포함한 합
            if max_v < s:
                max_v = s