N = int(input())
DAT = [0] * 10
cnt = 0
def func(row):
    global cnt

    if row == N:
        cnt += 1
        return
    for col in range(N):
        if DAT[col] == 1:
            continue
        DAT[col] = 1
        func(row + 1)
        DAT[col] = 0

func(0)
print(cnt)