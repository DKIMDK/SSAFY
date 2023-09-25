'''
봉우리
N*N 주어졌을 때
상하좌우 값 보다 크면 봉우리. 봉우리 모든 지역 찾아서 cnt
'''

def solution(N, arr):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]      # 상하좌우 방향을 저장
    cnt = 0
    for i in range(N):
        for j in range(N):                              # arr[i][j]를 순회
            max_num = 0
            for y, x in direction:
                dy, dx = i + y, j + x                   # 상하좌우를 search
                if 0 <= dx < N and 0 <= dy < N:          # arr의 range를 나가지 않는 선에서
                    if max_num <= arr[dy][dx]:           # arr[i][j] 상하좌우를 비교하여
                        max_num = arr[dy][dx]           # max_num에 최댓값을 저장

            if max_num < arr[i][j]:                     # 최댓값과 현재 위치를 비교하여 현재 위치가 크면
                cnt += 1                                # +1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = solution(N, arr)
    print(f'#{tc} {ans}')