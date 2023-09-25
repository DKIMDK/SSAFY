T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    answer = []

    for i in range(N):
        for j in range(N - M + 1):
            is_palindrome = True
            for k in range(M // 2):
                if arr[i][j + k] != arr[i][j + M - k - 1]:
                    is_palindrome = False
                    break
            if is_palindrome:
                answer = arr[i][j:j + M]

    for i in range(N - M + 1):
        for j in range(N):
            is_palindrome = True
            for k in range(M // 2):
                if arr[i + k][j] != arr[i + M - k - 1][j]:
                    is_palindrome = False
                    break
            if is_palindrome:
                answer = [arr[i + k][j] for k in range(M)]

    print(f'#{tc} {"".join(answer)}')
