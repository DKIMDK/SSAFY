def max_balloon_shooting_score(balloons):
    n = len(balloons)
    dp = [[0] * n for _ in range(n)]

    # Initialize the dp array for base cases (single balloons)
    for i in range(n):
        dp[i][i] = balloons[i]

    # Fill in the dp array for shooting sequences of balloons
    for length in range(2, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            max_score = 0

            # Consider each possible choice for the last balloon to shoot
            for last in range(start, end + 1):
                score = 1
                if start > 0:
                    score *= balloons[start - 1]
                if end < n - 1:
                    score *= balloons[end + 1]

                # Calculate the total score for this sequence
                if last > start:
                    score += dp[start][last - 1]
                if last < end:
                    score += dp[last + 1][end]

                max_score = max(max_score, score)

            dp[start][end] = max_score

    return dp[0][n - 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    balloons = list(map(int, input().split()))
    answer = max_balloon_shooting_score(balloons)
    print(f'#{tc} {answer}')
