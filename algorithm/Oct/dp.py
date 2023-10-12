def solution(N, balloons):
    max_score = 0

    def burst_balloon(index, score, remaining):
        nonlocal max_score

        if remaining == 0:
            max_score = max(max_score, score)
            return

        for i in range(N):
            if balloons[i] == -1:
                continue

            left = 1
            right = 1
            j = i - 1
            while j >= 0 and balloons[j] == -1:
                j -= 1
            if j >= 0:
                left = balloons[j]

            j = i + 1
            while j < N and balloons[j] == -1:
                j += 1
            if j < N:
                right = balloons[j]

            current_score = left * balloons[i] * right
            current_balloon = balloons[i]
            balloons[i] = -1  # 풍선을 터트림
            burst_balloon(index + 1, score + current_score, remaining - 1)
            balloons[i] = current_balloon  # 이전 상태로 복원

    burst_balloon(0, 0, N)
    return max_score

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    balloons = list(map(int, input().split()))
    answer = solution(N, balloons)
    print(f'#{tc} {answer}')
