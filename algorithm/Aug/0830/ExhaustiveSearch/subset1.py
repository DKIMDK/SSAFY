a = [1, 2, 3, 4]
N = 4

# for i in range(1, (1 << N) - 1):
for i in range(1, (1 << N) //2):
    group1 = []
    group2 = []
    total1 = 0
    total2 = 0
    for j in range(N):
        if i & (1 << j):            # j번 bit가 0이 아니면
            group1.append(a[j])
            total1 += a[j]
        else:
            group2.append(a[j])
            total2 += a[j]
    r1 = f(group1)
    r2 = f(group2)
    if r1 and r2:
        if min_v > abs(total1-total2):
    # print(group1, group2)
