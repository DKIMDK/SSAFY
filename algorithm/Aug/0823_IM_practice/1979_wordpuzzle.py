'''
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.
.

[제약 사항]
1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)
2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)


[입력]
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.


[출력]
테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

'''
#
# def solution():
#     direction = [(0, 1), (1, 0)]
#     cnt = 0
#     for y in range(N):
#         for x in range(N):
#             now = arr[y][x]
#             if now == 1:
#                 for dy, dx in direction:
#                     word = []  # 현재 위치에서 시작하는 단어 저장
#                     ny, nx = y, x
#                     while 0 <= ny < N and 0 <= nx < N:
#                         word.append(arr[ny][nx])
#                         ny, nx = ny + dy, nx + dx
#
#                     if len(word) == K and sum(word) == K:
#                         cnt += 1
#     return cnt
#
# T = int(input())
# for tc in range(1, T+1):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     ans = solution()
#     print(f'#{tc} {ans}')

# answer code
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N): # 행 검사
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N - 1 : # 현재 위치가 0이거나 마지막 열일경우
                if cnt == K:
                    result += 1
                cnt = 0
        for j in range(N): # 열검사
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N - 1: # 현재 위치가 0이거나 마지막 행일경우
                if cnt == K:
                    result += 1
                cnt = 0
    print(f'#{tc} {result}')