def col(N):
    global c
    if N == 1:
        return c
    elif N % 2 == 0:
        c += 1
        return col(N/2)
    else:
        c += 1
        return col(3*N + 1)
c = 0
# print(col(2))

def col(num, cnt):
    if num == 1:
        print(cnt)
        return
    if num % 2 == 0:
        col(num/2, cnt + 1)
    else:
        col((num*3) + 1, cnt + 1)

col(6, 0)