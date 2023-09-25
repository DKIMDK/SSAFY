T = int(input())
for tc in range(1, T + 1):
    A = [i for i in range(1, 13)]
    N, K = map(int, input().split())
    count = 0
    for i in range(1 << len(A)):
        sum_sub = 0
        subset = []
        for j in range(len(A)):
            if i & (1 << j):
                sum_sub += A[j]
                subset.append(A[j])

        if sum_sub == K and len(subset) == N:
            count += 1

    print(f'#{tc} {count}')
