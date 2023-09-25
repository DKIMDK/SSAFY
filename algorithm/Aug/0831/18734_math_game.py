A, B = map(int, input().split())
cnt = 0
while A != B:
    if B % 10 == 1:
        B //= 10
        cnt += 1
    if B % 2 == 0:
        B //= 2
        cnt += 1
    if (B % 2 == 1 and B % 10 != 1) or B < A:
        cnt = -1
        break


print(cnt)
