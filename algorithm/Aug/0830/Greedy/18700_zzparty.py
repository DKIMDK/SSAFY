N, M = map(int, input().split())
six_min = float('inf')
one_min = float('inf')
for _ in range(M):
    six, one = map(int, input().split())
    six_min = min(six_min, six)
    one_min = min(one_min, one)
if one_min * 6 < six_min:
    print(one_min * N)
else:
    buy = N // 6
    N %= 6
    if N * one_min > six_min:
        buy += 1
        print(buy * six_min)
    else:
        print(buy * six_min + N * one_min)

