T = int(input())
def recur(level, acc_height):
    global ans
    # 들어가기 전 (가지치기)
    if acc_height >= B:
        ans = min(ans, acc_height)

    # 기저 조건
    if level == N:
        return

    # 재귀 함수 호출

    # 해당 점원을 탑에 쓸 경우
    recur(level + 1, acc_height + arr[level])
    # 안 쓸 경우
    recur(level + 1, acc_height)



    # 돌아왔을 때

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = float('inf')
    recur(0, 0)
    print(f'#{tc} {ans - B}')