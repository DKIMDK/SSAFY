## 델타를 이용한 2차 배열 탐색
'''
3
1 2 3
4 5 6
7 8 9

'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # NXN 배열
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]  ## 중심을 기준으로 우, 하, 좌, 상

max_v = 0

for i in range(n):
    for j in range(n):
        s = arr[i][j]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n: ## 유효한 인덱스면, 가장자리에 있을 경우 오류 남을 방지
                print(arr[ni][nj])