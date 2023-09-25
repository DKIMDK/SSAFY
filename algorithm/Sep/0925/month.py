# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     P = list(input())
#     key = int(input(), 16)
#
#     H = [0]*N
#     for i in range(N):
#         H[i] = int(P[i], 16) ^ key
#     print(f'#{tc}', end = ' ')
#     for x in H:
#         print(f'{x:X}', end = '')
#     print()
# #
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     P = list(input())
#     Key = int(input(), 16)
#     for i in range(len(P)):
#         P[i] = int(P[i], 16)
#         P[i] = P[i] ^ Key
#         P[i] = str(P[i])
#         if P[i] == '10':
#             P[i] = 'A'
#         if P[i] == '11':
#             P[i] = 'B'
#         if P[i] == '12':
#             P[i] = 'C'
#         if P[i] == '13':
#             P[i] = 'D'
#         if P[i] == '14':
#             P[i] = 'E'
#         if P[i] == '15':
#             P[i] = 'F'
#     print(f'#{tc}', ''.join(P))

# 2 사격게임
# i: 현재 행, N: 전체 행의 수, s: 현재까지의 점수 합
def func(i, N, s):
    global max_v
    if i == N: # 모든 행을 다 본 경우
        if max_v < s:
            max_v = s

    else:
        for j in range(i, N): # 현재 행부터 마지막 행까지 순회
            p[i], p[j] = p[j], p[i]
            # 재귀 호출로 다음 행으로 넘어가며 점수를 더해주기
            func(i+1, N, s+arr[i][p[i]])
            # 백트래킹 (원래 순서로 다시 바꿔줌)
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]   # 초기 순서를 저장하는 리스트 p
    max_v = 0
    func(0, N, 0)
    print(f'#{tc} {max_v}')