def solution(num):
    num = str(num)
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    result = -1
    for i in range(N-1):
        for j in range(i+1, N):    # 2번 째 정수
            number = A[i] * A[j]
            if solution(number):
                result = max(result, number)

    print(f'#{tc} {result}')